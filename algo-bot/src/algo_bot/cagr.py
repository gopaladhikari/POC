from typing import cast

import yfinance as yf
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


def calculate_cagr(df: DataFrame, period: int = 365) -> DataFrame | float:
    if "Close" not in df.columns or len(df) < 2:
        return 0.0

    returns = df["Close"].pct_change().dropna()

    cum_return = (1 + returns).cumprod()

    final_cum_return = cum_return.iloc[-1]

    n = len(df) / period

    cagr = (final_cum_return) ** (1 / n) - 1

    return cagr


for ticker, data in ohcv_data.items():
    cagr_value = calculate_cagr(data, period=365)

    print(f"{ticker:8}: {cagr_value:.2%}")
