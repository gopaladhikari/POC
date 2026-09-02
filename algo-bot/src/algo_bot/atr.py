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


def ATR(DF: DataFrame, period: int = 14) -> DataFrame:
    df = DF.copy()
    prev_close = df["Close"].shift(1)

    h_l = df["High"] - df["Low"]
    h_pc = (df["High"] - prev_close).abs()
    l_pc = (df["Low"] - prev_close).abs()

    df["TR"] = h_l.combine(h_pc, max).combine(l_pc, max)

    df["ATR"] = df["TR"].ewm(alpha=1 / period, min_periods=period, adjust=False).mean()

    return df.loc[:, ["ATR"]]


for ticker, data in ohcv_data.items():
    atr_df = ATR(data)

    print(f"ATR for {ticker}:")

    print(atr_df.tail())

    print("\n")
