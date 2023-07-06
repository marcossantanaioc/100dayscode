import requests
import os
from data_manager import DataManager
from flight_data import FlightData
import json
import datetime as dt

TODAY = dt.datetime.today().date()
AHEAD = (TODAY + dt.timedelta(days=6*30))

class FlightSearch:
    # This class is responsible for talking to the Flight Search API.
    API_KEY = os.environ.get('KIWI_KEY')
    URL = "https://api.tequila.kiwi.com"

    def __init__(self):
        self.datamanager = DataManager()

    @property
    def header(self):
        return {'apikey': self.API_KEY}


    def get_iata_fromcity(self, city: str, output_langague: str = 'en-US', output_type: str = 'city'):

        params = {'term': city, 'locale': output_langague, 'location_types': output_type}
        response = requests.get(f"{self.URL}/locations/query", params=params, headers=self.header)
        response.raise_for_status()
        data = response.json()['locations']
        for res in data:
            if res['name'].lower() == city.lower():
                return res['code']

    def get_city_fromiata(self, iata: str, output_langague: str = 'en-US', output_type: str = 'city'):

        params = {'term': iata, 'locale': output_langague, 'location_types': output_type}
        response = requests.get(f"{self.URL}/locations/query", params=params, headers=self.header)
        response.raise_for_status()
        data = response.json()['locations']
        for res in data:
            if res['code'].lower() == iata.lower():
                return res['name']

    def search(self, city: str,
               destination: str,
               departure_from: str,
               departure_to: str):

        iata = self.get_iata_fromcity(city)
        destination_iata = self.get_iata_fromcity(destination)

        params = {'fly_from': iata,
                  'fly_to': destination_iata,
                  'curr': 'GBP',
                  'max_stopovers':0,
                  'one_per_city':1,
                  'date_from':departure_from,
                  'date_to':departure_to,
                  "nights_in_dst_from": 7,
                  "nights_in_dst_to": 28,
                  'sort': 'price'}

        response = requests.get(f"{self.URL}/search", params=params, headers=self.header)
        print(response.url)
        response.raise_for_status()
        return response.json()['data']#[0]


cities = ['Paris',
          'Berlin',
          'Tokyo',
          'Sydney',
          'Istanbul',
          'Kuala Lumpur',
          'New York',
          'San Francisco',
          'Cape Town']

# idx = 2
# datamanager = DataManager()
# searcher = FlightSearch()
# LOWEST_PRICE = 54
# res = searcher.search(city='London',
#                       destination='Paris',
#                       departure_from=TODAY.strftime("%d/%m/%Y"),
#                       departure_to=AHEAD.strftime("%d/%m/%Y"))

with open('test.json','r') as f:
    res = json.loads(f)
