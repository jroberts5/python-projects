'''
Overview: Checks the weather condition for a location(lat,lon) to see
if location will rain sends an text alert using twilio
'''

import requests
import os
from twilio.rest import Client

LATITUDE = "Enter Latitude"
LONGITUDE = "Enter Longitude"
# Apis keys saved through environment variables
WEATHER_API_KEY = os.environ['WEATHER_API_KEY']
account_sid = os.environ['TWILIO_ACCOUNT_SID']
auth_token = os.environ['TWILIO_AUTH_TOKEN']

response = requests.get(url=f"https://api.openweathermap.org/data/2.5/onecall?lat={LATITUDE}&lon={LONGITUDE}&exclude=current,minutely,daily,alerts&appid={WEATHER_API_KEY}")
weather_data = response.json()
# Takes the data from api and extracts the condition code
twelve_hour_forecast = [weather_data['hourly'][0]['weather'][0]['id'] for _ in range(12)]


# If condition code is less than 700 - will probably rain, thunderstorm, snow, etc.
will_rain = False
for code in twelve_hour_forecast:
    if int(code) < 700:
        will_rain = True

# Send SMS txt saying that it will rain today
if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
        body="It's going to rain today",
        from_='[Verified number in Twilio]',
        to='[whatever number]'
    )

response.raise_for_status()
