import os
from typing import Dict

import pandas as pd
import requests


class DataManager:
    # This class is responsible for talking to the Google Sheet.
    URL = f'https://api.sheety.co/a308f80c67a624a417930e2f946f5632/flightDeals/prices'
    TOKEN = os.environ.get('SHEETY_TOKEN')

    def __init__(self):
        response = requests.get(self.URL, headers=self.header)
        response.raise_for_status()
        self.raw = response.json()['prices']
        self.data = pd.DataFrame(self.raw, index=list(range(len(self.raw))))

    @property
    def columns(self):
        return self.data.columns

    @property
    def header(self) -> Dict:
        return {"Authorization": f"Bearer {self.TOKEN}"}

    def edit_entry(self, data: Dict, row_number: int):
        response = requests.put(f"{self.URL}/{row_number}", json=data, headers=self.header)
        response.raise_for_status()
        return response.text

    def get_iata(self, city: str) -> str:
        """
        Returns the IATA code for city.

        Parameters
        ----------
        city
            Name of a city.
        Returns
        -------
            IATA code.
        """
        return self.data[self.data['city'] == city.title()]['iataCode'].item()

    def get_city(self, iata: str) -> str:
        """
        Returns the city name for a given IATA code.
        Parameters
        ----------
        iata
            The IATA code for a city.

        Returns
        -------
            City name.
        """
        return self.data[self.data['iataCode'] == iata.upper()]['city'].item()
