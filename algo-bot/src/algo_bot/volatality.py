from typing import cast

import yfinance as yf
from numpy import sqrt
from pandas import DataFrame

cryptos = ["BTC-USD", "ETH-USD", "BNB-USD", "SOL-USD"]


ohcv_data: dict[str, DataFrame] = {}

temp = yf.download(tickers=cryptos, period="1mo", interval="15m")


if temp is not None and not temp.empty:
    temp.dropna(inplace=True, how="any")

    ohcv_data = {
        crypto: cast(DataFrame, temp.xs(crypto, level=1, axis=1)) for crypto in cryptos
    }

else:
    print("Error: No data was downloaded.")


def Volatility(DF: DataFrame) -> DataFrame:
    df = DF.copy()

    df["return"] = df["Close"].pct_change()

    df["volatility"] = df["return"].std() * sqrt(365)

    return df[["volatility"]]


for ticker, data in ohcv_data.items():
    volatility_df = Volatility(data)

    print(f"Volatility for {ticker}:")

    print(volatility_df.tail())

    print("\n")
