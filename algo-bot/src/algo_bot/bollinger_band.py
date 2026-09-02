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


def Bollinger_Band(DF: DataFrame, period=20, std=2):
    df = DF.copy()

    df["MA"] = df["Close"].rolling(window=period).mean()

    df["Upper"] = df["MA"] + df["Close"].rolling(window=period).std(ddof=0) * 2

    df["Lower"] = df["MA"] - df["Close"].rolling(window=period).std(ddof=0) * 2

    df["Width"] = df["Upper"] - df["Lower"]

    return df.loc[:, ["Upper", "Lower", "Width", "MA"]]


for ticker, data in ohcv_data.items():
    bollinger_band_df = Bollinger_Band(data)

    print(f"Bollinger Band for {ticker}:")

    print(bollinger_band_df.tail())

    print("\n")
