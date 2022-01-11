import requests
from datetime import datetime

# Constants
PIXELA_USERNAME = "[enter username]"
PIXELA_TOKEN = "[enter token key]"
PIXELA_ENDPOINT = "https://pixe.la/v1/users"
GRAPH_ID = "graph1"
REQUEST_HEADERS = {
    "X-USER-TOKEN": PIXELA_TOKEN
}

# Step 1 - Create user
user_params = {
    "token": PIXELA_TOKEN,
    "username": PIXELA_USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}
user_creation_response = requests.post(url=PIXELA_ENDPOINT, json=user_params)
print(user_creation_response.text)

# Step 2 - Creating the new graph
GRAPH_ENDPOINT = f"{PIXELA_ENDPOINT}/{PIXELA_USERNAME}/graphs"

graph_params = {
    "id": GRAPH_ID,
    "name": "Cycling Graph" ,
    "unit": "Mi" ,
    "type": "float",
    "color": "sora",
}

graph_creation_response = requests.post(url=GRAPH_ENDPOINT, json=graph_params, headers=request_headers)
print(graph_creation_response.text)

# Step 3 - Adding/updating quantity for the graph
quantity_endpoint = f"{PIXELA_ENDPOINT}/{PIXELA_USERNAME}/graphs/{GRAPH_ID}"

yesterday = datetime(year=2021, month=9, day=19).strftime('%Y%m%d')
today = datetime.now().strftime('%Y%m%d')
quantity_params = {
    "date": today,
    "quantity": input("Enter a quantity: "),
}

change_quantity_response = requests.post(url=quantity_endpoint, json=quantity_params, headers=REQUEST_HEADERS)
print(change_quantity_response.text)

# Optional - Delete graph
delete_quantity_response = requests.delete(url=quantity_endpoint, headers=REQUEST_HEADERS)
