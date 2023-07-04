from typing import Dict
import datetime as dt


class FlightData:
    """
    This class is responsible for structuring the flight data.
    At the moment it can only deal with direct inbound and outbound flights.

    # TODO add support for single flight and multiple routes.

    Attributes
    ----------
    route
        A list of dictionaries where each element is a another dictionary with the flight route.
        The first element of route is the inbound flight and the second element the outbound.
    """

    def __init__(self, data: Dict):
        self.route = data['route']
        self.price = data['price']

    @property
    def inbound(self):
        return self.route[0]

    @property
    def outbound(self):
        return self.route[1]

    def format_flight(self, flight: Dict):
        departure_city = f"{flight['cityFrom']}-{flight['flyFrom']}"
        arrival_city = f"{flight['cityTo']}-{flight['flyTo']}"
        departure_time = f"{dt.datetime.fromtimestamp(flight['dTime']).strftime('%Y/%m/%d-%H:%M:%S')}"
        arrival_time = f"{dt.datetime.fromtimestamp(flight['aTime']).strftime('%Y/%m/%d-%H:%M:%S')}"
        return {'departure': {'city': departure_city,
                              'time': departure_time},
                'arrival': {'city': arrival_city, 'time': arrival_time}}
