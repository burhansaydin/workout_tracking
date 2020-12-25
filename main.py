import requests
from datetime import datetime
import os

today = datetime.now()
today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")
APP_ID = os.environ["api_id"]
API_KEY = os.environ["api_key"]
WEIGHT = 70
HEIGHT = 178
AGE = 26
GENDER = "male"
project_name = "workoutTracking"
USER_NAME = "edf085e32a6ddaf9769cd34d744415d7"
SHEET_NAME = "workouts"
authentication = os.environ["auth"]

query = input("Tell me which exercises you did: ")

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
    "Content-Type": "application/json"
}
params_nutr = {
    "query": query,
    "gender": GENDER,
    "weight_kg": WEIGHT,
    "height_cm": HEIGHT,
    "age": AGE,
}
header= {
    "Authorization": F"Bearer {authentication}"
}


nutritionix_endpoint = " https://trackapi.nutritionix.com/v2/natural/exercise"
sheety_endpoint = os.environ["sheet_end"]


response = requests.post(url=nutritionix_endpoint, json=params_nutr, headers=headers)
result = response.json()
print(result)


for exercise in result["exercises"]:
    sheet_inputs = {
        "workout": {
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

    sheet_response = requests.post(sheety_endpoint, json=sheet_inputs, headers=header)

    print(sheet_response.text)
