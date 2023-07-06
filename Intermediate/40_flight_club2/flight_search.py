import requests
import os
from typing import List, Dict, Any


class FlightSearch:
    """
    This class is responsible for talking to the Flight Search API.
    """
    API_KEY = os.environ.get('KIWI_KEY')
    URL = "https://api.tequila.kiwi.com"

    @property
    def header(self) -> Dict:
        """
        Returns the header for the API call
        """
        return {'apikey': self.API_KEY}

    def get_iata_fromcity(self, city: str):
        """
        Get the IATA code from a city name.
        This will send a GET request to tequila using the city name as a query.

        Parameters
        ----------
        city
            The city name.
        Returns
        -------
            IATA code.
        """

        params = {'term': city, 'locale': 'en-US', 'location_types': 'city'}
        response = requests.get(f"{self.URL}/locations/query", params=params, headers=self.header)
        response.raise_for_status()
        data = response.json()['locations']
        for res in data:
            if res['name'].lower() == city.lower():
                return res['code']

    def get_city_fromiata(self, iata: str):
        """
        Get the city name from IATA code.
        This will send a GET request to tequila using the IATA code as a query.

        Parameters
        ----------
        iata
            The IATA code for a city.
        Returns
        -------
           City name.
        """

        params = {'term': iata, 'locale': 'en-US', 'location_types': 'city'}
        response = requests.get(f"{self.URL}/locations/query", params=params, headers=self.header)
        response.raise_for_status()
        data = response.json()['locations']
        for res in data:
            if res['code'].lower() == iata.lower():
                return res['name']

    def search(self, city: str,
               destination: str,
               departure_from: str,
               departure_to: str) -> List[Dict[Any, Any]]:

        """
        Searches tequila/kiwi for flight deals.
        """

        print(f"Looking flights to {destination}.")
        iata = self.get_iata_fromcity(city)
        destination_iata = self.get_iata_fromcity(destination)

        params = {'fly_from': iata,
                  'fly_to': destination_iata,
                  'curr': 'GBP',
                  'max_stopovers': 0,
                  'one_per_city': 1,
                  'date_from': departure_from,
                  'date_to': departure_to,
                  "nights_in_dst_from": 7,
                  "nights_in_dst_to": 28,
                  'sort': 'price'}

        response = requests.get(f"{self.URL}/search", params=params, headers=self.header)
        response.raise_for_status()
        return response.json()['data'][0]
