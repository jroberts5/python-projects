from twilio.rest import Client
import os

TWILIO_ACCOUNT_SID = os.environ['TWILIO_ACCOUNT_SID']
TWILIO_AUTH_TOKEN = os.environ['TWILIO_AUTH_TOKEN']
TWILIO_NUMBER = "[verified twilio phone number]"
PHONE_NUMBER = "[some phone number]"


class NotificationManager:
    # This class is responsible for sending notifications with the deal flight details.
    def __init__(self):
        self.origin = "Charlotte"
        self.origin_code = "CLT"

    def send_sms(self, departure, arrival, destination, cost):
        client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)
        message = client.messages \
            .create(
            body=f"Low price alert!From {self.origin} to {destination}: ${cost}\n Departure: {departure} Arrival:{arrival}",
            from_=f"{TWILIO_NUMBER}",
            to=f"{PHONE_NUMBER}"
        )
        print(message.status)
