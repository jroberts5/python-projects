# Module Imports
from data_manager import DataManager
from flight_search import FlightSearch
from notification_manager import NotificationManager


flight_manager = FlightSearch()
spreadsheet_manager = DataManager()
sms_manager = NotificationManager()

# Retrieves data from google spreadsheets - updates spreadsheet for each location
spreadsheet_data = spreadsheet_manager.get_spreadsheet_data()
for location in spreadsheet_data["prices"]:
    if location["iataCode"] == '':
        iata_code = flight_manager.get_iata_codes(location)
        location["iataCode"] = iata_code
        # Update the IATA Codes for each city
        spreadsheet_manager.update_spreadsheet_data(location)

    # Searchs flights
    flight_info = flight_manager.get_flight_info(location)
    flight_cost = flight_info[0]
    flight_departure = flight_info[1]
    flight_arrival = flight_info[2]
    if flight_cost < location['lowestPrice']:
        sms_manager.send_sms(departure=flight_departure,
                             arrival=flight_arrival,
                             destination=location["city"],
                             cost=flight_cost)

