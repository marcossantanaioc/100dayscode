import os
from twilio.rest import Client
import pandas as pd
import requests
import datetime as dt
from typing import Dict, Union, List

URL = "https://www.alphavantage.co/query"
NEWS_URL = "http://api.mediastack.com/v1/news"
client = Client(os.environ['TWILLIO_SID'], os.environ['TWILLIO_TOKEN'])
STOCK = "TSLA"
COMPANY_NAME = "Tesla"
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
        return {'function': 'TIME_SERIES_DAILY_ADJUSTED', 'symbol': self.stock_symbol, 'apikey': self.api_key}

    @property
    def today(self):
        return dt.datetime.today().date()

    def get_daily_info(self, outputsize: str = 'compact', output_format: str = 'json'):
        params = self.daily_params
        params['outputsize'] = outputsize
        params['datatype'] = output_format
        response = requests.get(self.URL, params)
        response.raise_for_status()
        data = response.json()['Time Series (Daily)']

        return data

    def get_stock_change(self, first_date: str, second_date: str):
        data = self.get_daily_info()
        first_date_stock = Stock(data[first_date])
        second_date_stock = Stock(data[second_date])
        return first_date_stock, second_date_stock

    def get_news(self, keyword: str, dates: Union[List[str], str]):
        if isinstance(dates, list):
            dates = ",".join(dates)
        params = {"access_key": os.environ.get("MEDIASTACKKEY"),
                  "date": dates,
                  "keywords": keyword,
                  "language": "en",
                  "countries": "us",
                  "sources": "-etfdailynews",
                  "sort": "popularity",
                  "limit": 100}

        response = requests.get(url=NEWS_URL, params=params)
        response.raise_for_status()
        news_data = pd.DataFrame(response.json()["data"])
        filtered_news = news_data[news_data['description'].str.contains(keyword)]
        return filtered_news


if __name__ == '__main__':
    stock_monitor = StockMonitor(STOCK, APIKEY)
    first_date = (TODAY - dt.timedelta(days=1)).strftime("%Y-%m-%d")
    second_date = (TODAY - dt.timedelta(days=2)).strftime("%Y-%m-%d")

    first_stock, second_stock = stock_monitor.get_stock_change(first_date=first_date, second_date=second_date)

    variation = [first_stock.close - 0.05 * first_stock.close, first_stock.close + 0.05 * first_stock.close]

    if second_stock.close <= variation[0] or second_stock.close >= variation[1]:
        print('Get News')
    else:
        variation = 1 - (first_stock.close / second_stock.close)
        if variation >= 0:
            symbol = "🔺"
        else:
            symbol = "🔻"

        variation_message = f"{symbol} {variation:.2f}%"
        print("Don't get news")
        news_data = stock_monitor.get_news(keyword=COMPANY_NAME, dates=[first_date, second_date])
        news_message = f"{COMPANY_NAME} {variation_message}\n" \
                       f"Headline: {news_data.loc[0]['title']}\nBrief: {news_data.loc[0]['description']}"

        message = client.messages.create(
            body=news_message,
            from_='whatsapp:+14155238886',
            to='whatsapp:+5521996766769'
        )
        print(message.status)
