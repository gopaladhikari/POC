from typing import cast

import yfinance as yf
from numpy import sqrt
from pandas import DataFrame

cryptos = ["BTC-USD", "ETH-USD", "BNB-USD", "SOL-USD"]

ohcv_data: dict[str, DataFrame] = {}

temp = yf.download(tickers=cryptos, period="1y", interval="1d")


if temp is not None and not temp.empty:
    temp.dropna(inplace=True, how="any")

    ohcv_data = {
        crypto: cast(DataFrame, temp.xs(crypto, level=1, axis=1)) for crypto in cryptos
    }

else:
    print("Error: No data was downloaded.")


def Cagr(df: DataFrame, period: int = 365) -> DataFrame | float:
    if "Close" not in df.columns or len(df) < 2:
        return 0.0

    returns = df["Close"].pct_change().dropna()

    cum_return = (1 + returns).cumprod()

    final_cum_return = cum_return.iloc[-1]

    n = len(df) / period

    cagr = (final_cum_return) ** (1 / n) - 1

    return cagr


def Volatility(DF: DataFrame) -> DataFrame:
    df = DF.copy()

    df["return"] = df["Close"].pct_change()

    df["volatility"] = df["return"].rolling(window=30).std() * sqrt(365) * 100

    return df[["volatility"]]


def SharpeRatio(DF: DataFrame, period: int = 365) -> DataFrame | float:
    volatility = Volatility(DF)

    sharpe = (Cagr(DF, period) - 0.03) / volatility

    return sharpe


for ticker, data in ohcv_data.items():
    sharpe_ratio = SharpeRatio(data)

    print(f"Sharpe Ratio for {ticker}: is {sharpe_ratio}")
