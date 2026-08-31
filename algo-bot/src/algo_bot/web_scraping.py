import requests
from bs4 import BeautifulSoup

url = "https://finance.yahoo.com/quote/AAPL/financials/"


headers = {"User-Agent": "Mozilla/5.0"}

res = requests.get(url, headers=headers)

soup = BeautifulSoup(res.text, "html.parser")

tables = soup.find_all("table")

if tables:
    print(f"Found {len(tables)} table(s).")
    # Print a snippet of the first table's text to verify
    print(tables[0].text[:500])
else:
    print("No tables found. Data may be JavaScript-rendered.")
