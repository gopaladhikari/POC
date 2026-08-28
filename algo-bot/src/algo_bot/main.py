import yfinance as yf
from datetime import datetime, timedelta
import pandas as pd

cryptos = ["BTC-USD", "ETH-USD", "BNB-USD", "SOL-USD"]

start = datetime.today() - timedelta(360)

end = datetime.today()


def main():
    cl_price = pd.DataFrame()

    for ticker in cryptos:
        data = yf.download(tickers=ticker, start=start, end=end)

        if data is not None and not data.empty:
            cl_price = data["Close"]

            print(cl_price)

        else:
            print("Error: No data was downloaded.")
