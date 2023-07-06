import datetime as dt
import json
class FlightData:

    def __init__(self, data):
        self.data = data['route']
        self.price = data['conversion']['GBP']
        self.departure_airport_code = self.data[0]['flyFrom']
        self.departure_city = self.data[0]['cityFrom']
        self.arrival_airport_code = self.data[0]['flyTo']
        self.arrival_city = self.data[0]['cityTo']
        self.departure_time = dt.datetime.fromtimestamp(self.data[0]['dTime']).strftime('%Y-%m-%d')
        self.arrival_time = dt.datetime.fromtimestamp(self.data[0]['aTime']).strftime('%Y-%m-%d')

        self.return_departure_airport_code = self.data[1]['flyFrom']
        self.return_departure_city = self.data[1]['cityFrom']
        self.return_arrival_airport_code = self.data[1]['flyTo']
        self.return_arrival_city = self.data[1]['cityTo']
        self.return_departure_time = dt.datetime.fromtimestamp(self.data[1]['dTime']).strftime('%Y-%m-%d')
        self.return_arrival_time = dt.datetime.fromtimestamp(self.data[1]['aTime']).strftime('%Y-%m-%d')

    def __str__(self):
        return f"{self.departure_city}-{self.departure_airport_code} to {self.arrival_city}-{self.arrival_airport_code}, from {self.departure_time} to {self.return_departure_time}"

with open('test.json','r') as f:
    data = json.load(f)

flightdata = FlightData(data)
print(flightdata)
