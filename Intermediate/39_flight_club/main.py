import os
import requests
#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.

SHEETY_TOKEN = os.environ.get('SHEETY_TOKEN')
SHEETY_URL = "https://api.sheety.co/a308f80c67a624a417930e2f946f5632/flightDeals/prices"

# Get sheety data
header = {"Authorization": "Bearer XXXXXXXXXXXXX"}
response = requests.get(SHEETY_URL,  headers=header)
response.raise_for_status()
sheet_data = response.json()['prices']
print(sheet_data)
city_names = []
for info in sheet_data:
    city_names.append(info['city'])
print(city_names)