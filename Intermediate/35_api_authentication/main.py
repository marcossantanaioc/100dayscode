import requests
import os
from twilio.rest import Client


# Openweather configuration

LAT = 53.34
LON = 10.0
URL = f"https://api.openweathermap.org/data/3.0/onecall"

client = Client(os.environ['TWILLIO_SID'], os.environ['TWILLIO_TOKEN'])

# Request
params = {'lat': LAT,
          'lon': LON,
          'appid': os.environ['WEATHER_KEY']}

response = requests.get(URL, params=params)


response.raise_for_status()
weather_data = response.json()['hourly'][:12]
WILL_RAIN = False


for hour_index, hour in enumerate(weather_data):
    next_hour_forecast = hour['weather'][0]
    if next_hour_forecast['id'] < 700:
       WILL_RAIN = True


if WILL_RAIN:
    message = client.messages.create(
                                  body='Bring an umbrella because it will rain!',
                                  from_='whatsapp:XXXXXXXXXXXXXXXX',
                                  to='whatsapp:XXXXXXXXXXXXXXXXXXX'
                              )
    print(message.status)