from data_manager import DataManager
from flight_data import FlightData
from flight_search import FlightSearch
import datetime as dt
from notification_manager import NotificationManager

TODAY = dt.datetime.today().date()
AHEAD = (TODAY + dt.timedelta(days=6 * 30))

cities = ['Paris',
          'Berlin',
          'Tokyo',
          'Sydney',
          'Istanbul',
          'Kuala Lumpur',
          'New York',
          'San Francisco',
          'Cape Town']

datamanager = DataManager()
searcher = FlightSearch()
notification_manager = NotificationManager()

for city in cities:
    res = searcher.search(city='London',
                          destination=city,
                          departure_from=TODAY.strftime("%d/%m/%Y"),
                          departure_to=AHEAD.strftime("%d/%m/%Y"))

    flightdata = FlightData(res)

    # Get price threshold
    lowest_price = datamanager.get_city(city)['lowestPrice'].item()

    print(f"Price threshold for {city} = {lowest_price} | Price: {flightdata.price}")

    if flightdata.price <= lowest_price:
        inbound_flight = flightdata.format_flight(flightdata.inbound)
        outbound_flight = flightdata.format_flight(flightdata.outbound)
        message = f"Low price alert!\nOnly £{flightdata.price} to fly from" \
                  f" \n{inbound_flight['departure']['city']} to {inbound_flight['arrival']['city']}," \
                  f" from\n{flightdata.inbound_date} to {flightdata.outbound_date}"

        print(message)

        msg = notification_manager.send(message=message, from_number='+14155238886', to_number='+5521996766769')
        print(msg.status)
