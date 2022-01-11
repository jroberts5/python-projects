import requests
import os
import datetime

TEQUILA_ENDPOINT = "https://tequila-api.kiwi.com"
TEQUILA_FLIGHT_SEARCH_API_KEY = os.environ['TEQUILA_FLIGHT_SEARCH_API_KEY']
TODAY = datetime.date.today()


class FlightSearch:
    def __init__(self):
        self.response_header = {
            "apikey": TEQUILA_FLIGHT_SEARCH_API_KEY,
        }
        self.current_date = datetime.datetime.now()
        self.tomorrow = (datetime.datetime.now() + datetime.timedelta(days=1))
        self.date_six_months = (datetime.datetime.now() + datetime.timedelta(days=365.25 / 2))
        self.origin = "Charlotte"
        self.origin_code = "CLT"

    def get_iata_codes(self, city):
        location_search_params = {
            "term": city['city'],
        }
        location_search_endpoint = f"{TEQUILA_ENDPOINT}/locations/query"
        tequila_response = requests.get(url=location_search_endpoint, headers=self.response_header, params=location_search_params)
        location_data = tequila_response.json()
        location_code = location_data['locations'][0]["code"]
        return location_code


    def get_flight_info(self, city):
        flight_search_endpoint = f"{TEQUILA_ENDPOINT}/v2/search"
        flight_search_params = {
            "fly_from": self.origin_code,
            "fly_to": city['iataCode'],
            "date_from": self.tomorrow.strftime("%d/%m/%Y"),
            "date_to": self.date_six_months.strftime("%d/%m/%Y"),
            "curr": "USD"
        }
        tequila_response = requests.get(url=flight_search_endpoint, params=flight_search_params, headers=self.response_header)
        flight_search_data = tequila_response.json()
        flight_cost = flight_search_data['data'][0]['price']
        flight_departure = flight_search_data["data"][0]['route'][0]['local_departure'].split("T")[0]
        flight_arrival = flight_search_data["data"][0]["route"][-1]['local_arrival'].split("T")[0]
        return flight_cost, flight_departure, flight_arrival
