
import yfinance as yf

ticker = "MSFT"
company = yf.Ticker(ticker)

try:
    isin = company.isin
    print(isin)
except Exception as e:
    print(f"An error occurred: {e}")
