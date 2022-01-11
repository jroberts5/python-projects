import requests
from datetime import datetime
import smtplib
import time

# Constants
EMAIL = 'testemail15624234@gmail.com'
PASSWORD = '*************'
MY_LAT = 35.223789  # Your latitude
MY_LONG = -80.841141  # Your longitude

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()

iss_latitude = float(data["iss_position"]["latitude"])
iss_longitude = float(data["iss_position"]["longitude"])


def send_email():
    connection = smtplib.SMTP('smtp.gmail.com')
    connection.starttls()
    connection.login(EMAIL, PASSWORD)
    connection.sendmail(
        from_addr=EMAIL,
        to_addrs=EMAIL,
        msg="Subject: Look up!\n\n The ISS is above you in the sky"
    )


def iss_overhead():
    if MY_LAT - 5 <= iss_latitude <= MY_LAT + 5 and MY_LONG -5  <= iss_longitude <= MY_LONG + 5:
        return True


def is_night():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }
    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])
    current_time = datetime.now().hour

    if current_time >= sunset or current_time <= sunrise:
        return True

# Start
while True:
    time.sleep(60)
    if iss_overhead() and is_night():
        send_email()


