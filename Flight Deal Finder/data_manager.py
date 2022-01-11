import os
import requests

SHEETY_ENDPOINT = os.environ['SHEETY_ENDPOINT']
SHEETY_BASE64_PW = os.environ['SHEETY_BASE64_PW']


class DataManager:
    def __init__(self):
        self.sheety_headers = {
            "Authorization": SHEETY_BASE64_PW,
        }

    def get_spreadsheet_data(self):
        sheety_get_response = requests.get(url=SHEETY_ENDPOINT, headers=self.sheety_headers)
        sheety_data = sheety_get_response.json()
        return sheety_data

    def update_spreadsheet_data(self, city):
        sheety_update_endpoint = f"{SHEETY_ENDPOINT}/{city['id']}"
        sheety_update_params = {
            'price': {
                "city": city['city'],
                "iataCode": city['iataCode'],
                "lowestPrice": city['lowestPrice']
            }
        }
        sheety_update_response = requests.put(url=sheety_update_endpoint, json=sheety_update_params, headers=self.sheety_headers)
        print(sheety_update_response.text)



