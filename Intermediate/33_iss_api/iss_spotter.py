import requests
from datetime import datetime
import smtplib
import time

MY_LAT = 51.752022  # Your latitude
MY_LONG = -1.257726  # Your longitude
EMAIL = 'marcosvssantana@gmail.com'
PASSWORD = 'vkiqoqsxeyxqqbtp'


def get_iss_position():
    global response, data
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()
    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])
    return iss_longitude, iss_latitude


iss_longitude, iss_latitude = get_iss_position()

# Your position is within +5 or -5 degrees of the ISS position.

parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}


def check_is_dark():
    global response, data
    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])
    time_now = datetime.now().hour
    if (time_now >= sunset) and (time_now <= sunrise):
        return True
    return False


def find_iss(current_lat: float, current_log: float, iss_current_lat: float, iss_current_log: float):
    lat_range = [current_lat - 5, current_lat + 5]
    log_range = [current_log - 5, current_log + 5]

    if (lat_range[0] <= iss_current_lat <= lat_range[1]) and (log_range[0] <= iss_current_log <= log_range[1]):
        return True
    else:
        return False


is_dark = check_is_dark()
is_in_range = find_iss(current_lat=MY_LAT, current_log=MY_LONG, iss_current_lat=iss_latitude,
                       iss_current_log=iss_longitude)

RUN = True
while RUN:
    # if not is_dark and not is_in_range:
    # # If the ISS is close to my current position
    # # and it is currently dark
    # # Then send me an email to tell me to look up.
    # # BONUS: run the code every 60 seconds.

    with smtplib.SMTP(host='smtp.gmail.com') as connection:
        # Put the SMTP connection in TLS (Transport Layer Security) mode.
        # All SMTP commands that follow will be encrypted.
        connection.starttls()

        connection.login(user='marcosvssantana@gmail.com', password=PASSWORD)

        connection.sendmail(from_addr=EMAIL,
                            to_addrs=EMAIL,
                            msg='Subject:ISS spotter\nThe ISS is over your position')

    time.sleep(60)
