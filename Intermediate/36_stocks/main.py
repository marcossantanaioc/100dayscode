import os
import requests
import datetime as dt
from typing import Dict

URL = "https://www.alphavantage.co/query"
STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
TODAY = dt.datetime.today().date()
APIKEY = os.environ.get('ALPHAVANTAGE')


class Stock:
    def __init__(self, stock_info: Dict):
        self.stock_info = stock_info
        for key, value in stock_info.items():
            formatted_key = key.split('. ')[1]
            setattr(self, formatted_key, float(value))

class StockMonitor:
    def __init__(self, stock_symbol: str, api_key: str):
        self.URL = "https://www.alphavantage.co/query"
        self.stock_symbol = stock_symbol
        self.api_key = api_key

    @property
    def daily_params(self):
        return {'function': 'TIME_SERIES_DAILY_ADJUSTED', 'symbol':self.stock_symbol, 'apikey': self.api_key}

    @property
    def today(self):
        return dt.datetime.today().date()

    def get_daily_info(self, outputsize: str = 'compact', format: str = 'json'):
        params = self.daily_params
        params['outputsize'] = outputsize
        params['datatype'] = format
        response = requests.get(self.URL, params)
        response.raise_for_status()
        data = response.json()['Time Series (Daily)']
        return data

    def get_stock_change(self, first_date: str, second_date: str):
        data = self.get_daily_info()
        first_date_stock = Stock(data[first_date])
        second_date_stock = Stock(data[second_date])
        return first_date_stock, second_date_stock

## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
stock_monitor = StockMonitor(STOCK, APIKEY)
first_stock, second_stock = stock_monitor.get_stock_change(first_date='2023-06-30',second_date='2023-06-29')

variation = [first_stock.close - 0.05 * first_stock.close, first_stock.close + 0.05 * first_stock.close]
if second_stock.close <= variation[0] or second_stock.close >= variation[1]:
    print('Get News!')
else:
    print("Don't get news")


## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 

## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number. 


# Optional: Format the SMS message like this:
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""
