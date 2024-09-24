import yfinance as yf


ticker = input("Enter the ticker")
from_data = input("enter the start date(yyyy-mm-dd):")
to_date = input("enter the end date(yyyy-mm-dd)")


stock_data = yf.download(ticker,start=from_data,end=to_date)
stock_data.to_csv("stock_data.html")
print("stock data written as stock_data.html")