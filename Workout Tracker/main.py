
'''
Overview: Takes a workout input, converts input using Nutrition Exercise API
to extract the workout name,duration, and calories burned in the workout. Sends
extracted data to sheety which adds a new row(workout) to Google Sheet.
'''

import requests
import os
from datetime import datetime

add_workout = True
TITLE = "Welcome to Workout Tracker!"
# Nutritionix Config
NUTRITIONIX_ENDPOINT = "https://trackapi.nutritionix.com/v2/natural/exercise"
NUTRITIONIX_APP_ID = os.environ["NUTRITIONIX_APP_ID"]
NUTRITIONIX_API_KEY = os.environ["NUTRITIONIX_API_KEY"]
GENDER = '[gender]'
WEIGHT_KG = 0
HEIGHT_CM = 0
AGE = 0

# Sheety Config
SHEETY_ENDPOINT = "https://api.sheety.co/15a3fef44c2b40b156dbd7aa9161bfb6/myWorkouts/workouts"
SHEETY_BASE64_PW = os.environ["SHEETY_BASE64_PW"]
CURRENT_DATE = datetime.now().strftime("%d/%m/%Y")
CURRENT_TIME = datetime.now().strftime("%X")

print(TITLE)

while add_workout:
    # Adds new work out and then sends request to Nutritionix
    nutritionix_add_workout_params = {
        "query": input("\nType the workout you did: "),
        "gender": GENDER,
        "weight_kg": WEIGHT_KG,
        "height_cm": HEIGHT_CM,
        "age": AGE,
    }
    nutritionix_headers = {
        "x-app-id": NUTRITIONIX_APP_ID,
        "x-app-key": NUTRITIONIX_API_KEY,
    }
    try:
        nutritionix_response = requests.post(url=NUTRITIONIX_ENDPOINT,
                                             json=nutritionix_add_workout_params,
                                             headers=nutritionix_headers)
        n_result = nutritionix_response.json()
    except Exception:
        raise Exception("Error occurred when sending or receiving data from Nutritionix API")
    else:
        print("Data sent and received successfully from Nutritionix API.")

    # Extracts data from Nutritionix, saves into a dict for the new workout
    new_workout = {
        "name": n_result['exercises'][0]['name'],
        "duration": n_result['exercises'][0]['duration_min'],
        "calories": n_result['exercises'][0]['nf_calories'],
    }

    # Sends extracted data to Sheety - adds a new row into the Google Sheet project
    sheety_add_params = {
        "workout": {
            "date": CURRENT_DATE,
            "time": CURRENT_TIME,
            "exercise": new_workout["name"].title(),
            "duration": new_workout["duration"],
            "calories": new_workout["calories"],
        }
    }
    sheety_headers = {
        "Authorization": SHEETY_BASE64_PW
    }
    try:
        sheety_response = requests.post(url=SHEETY_ENDPOINT,
                                        json=sheety_add_params,
                                        headers=sheety_headers)
    except Exception:
        raise Exception("Error occurred when sending or receiving data from Sheety API")
    else:
        print('Workout successfully added!')

    # Asks if user would like to enter another workout
    another_workout = input("Would you like to enter another workout?: Type 'yes' or 'no': ")

    if another_workout == 'yes':
        continue
    elif another_workout == 'no':
        print('Goodbye.')
        add_workout = False
