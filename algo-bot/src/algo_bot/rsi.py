from typing import cast

import yfinance as yf
from numpy import where
from pandas import DataFrame

cryptos = ["BTC-USD", "ETH-USD", "BNB-USD", "SOL-USD"]

ohcv_data: dict[str, DataFrame] = {}

temp = yf.download(tickers=cryptos, period="1mo", interval="5m")


if temp is not None and not temp.empty:
    temp.dropna(inplace=True, how="any")

    ohcv_data = {
        crypto: cast(DataFrame, temp.xs(crypto, level=1, axis=1)) for crypto in cryptos
    }

else:
    print("Error: No data was downloaded.")


def RSI(data: DataFrame, period: int = 14) -> DataFrame:
    """
    Calculates the Relative Strength Index (RSI) for a given period.

    Parameters:
    - odata (DataFrame): The input data to calculate the RSI for.
    - period (int): The perid for which the RSI will be calculated. Default is 14.

    Returns:
    - DataFrame: The RSI values for the given period.
    """

    df = data.copy()

    df["Change"] = df["Close"] - df["Close"].shift(1)

    df["gain"] = where(df["Change"] > 0, df["Change"], 0)

    df["loss"] = where(df["Change"] < 0, -1 * df["Change"], 0)

    df["avg_gain"] = df["gain"].ewm(alpha=1 / period, min_periods=period).mean()

    df["avg_loss"] = df["loss"].ewm(alpha=1 / period, min_periods=period).mean()

    df["RS"] = df["avg_gain"] / df["avg_loss"]

    df["RSI"] = 100 - (100 / (1 + df["RS"]))

    return df.loc[:, ["RSI", "avg_gain", "avg_loss", "RS", "Change", "gain", "loss"]]


for ticker, data in ohcv_data.items():
    rsi_df = RSI(data)

    print(f"RSI for {ticker}:")

    print(rsi_df.tail())

    print("\n")
