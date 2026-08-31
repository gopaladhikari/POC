from datetime import UTC, datetime, timedelta

import matplotlib.pyplot as plt
import pandas as pd
import yfinance as yf

cryptos = ["BTC-USD", "ETH-USD", "BNB-USD", "SOL-USD"]

end = datetime.now(UTC)

start = end - timedelta(days=1000)


def main():
    cl_price = pd.DataFrame()

    data = yf.download(tickers=cryptos, start=start, end=end)

    if data is not None and not data.empty:
        cl_price = data["Close"]

        cl_price.dropna(inplace=True, axis=0, how="any")

        daily_return = cl_price.pct_change()

        _fig, axes = plt.subplots()

        axes.set_title("Daily Return")
        axes.set_xlabel("Crypto")
        axes.set_ylabel("Mean Return")

        plt.bar(x=daily_return.columns, height=daily_return.mean())

        plt.show()

    else:
        print("Error: No data was downloaded.")
