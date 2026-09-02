from typing import cast

import yfinance as yf
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


def ATR(DF: DataFrame, period=14):
    df = DF.copy()

    df["H-L"] = df["High"] - df["Low"]

    df["H-PC"] = df["High"] - df["Close"].shift(1)

    df["L-PC"] = df["Low"] - df["Close"].shift(1)

    df["TR"] = df[["H-L", "H-PC", "L-PC"]].max(axis=1, skipna=False)

    df["ATR"] = df["TR"].ewm(span=period, min_periods=period).mean()

    return df.loc[:, ["ATR"]]


for ticker, data in ohcv_data.items():
    atr_df = ATR(data)

    print(f"ATR for {ticker}:")

    print(atr_df.tail())

    print("\n")
