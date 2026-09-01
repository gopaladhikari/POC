from typing import cast

import yfinance as yf
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


def MACD(DF: DataFrame, fast_line=12, slow_line=26, signal_line=9):
    df = DF.copy()

    df["MA_Fast"] = df["Close"].ewm(span=fast_line, min_periods=fast_line).mean()

    df["MA_Slow"] = df["Close"].ewm(span=slow_line, min_periods=slow_line).mean()

    df["MACD"] = df["MA_Fast"] - df["MA_Slow"]

    df["Signal"] = df["MACD"].ewm(span=signal_line, min_periods=signal_line).mean()

    return df.loc[:, ["MACD", "Signal"]]


for ticker, data in ohcv_data.items():
    macd_df = MACD(data)

    print(f"MACD for {ticker}:")

    print(macd_df.tail())

    print("\n")
