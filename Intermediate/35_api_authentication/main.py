import requests
import pandas as pd


API_KEY = "1a9b78c971ff4eb87ff6531b09f44cd1"
LAT = 51.758360
LON = -1.216770
URL = f"https://api.openweathermap.org/data/3.0/onecall"
params = {'lat':LAT,
          'lon':LON,
          'appid': API_KEY}
print(URL)

response = requests.get(URL, params=params)
response.raise_for_status()
print(response)