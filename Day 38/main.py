import requests
from datetime import datetime

import os
from dotenv import find_dotenv, load_dotenv

GENDER = "male"
WEIGHT_KG = "69"
HEIGHT_CM = "169"
AGE = "22"

# mencari lokasi file .env secara otomatis 
dotenv_path = find_dotenv()

# load the entries as environtment variables
load_dotenv(dotenv_path)

# stored the env variables within a python variable
APP_ID = os.getenv("APP_ID")
API_KEY = os.getenv("API_KEY")

print(API_KEY)

endpoint = "https://trackapi.nutritionix.com"

excercise_endpoints = f"{endpoint}/v2/natural/exercise"

headers_nutrition = {
    "x-app-id" : APP_ID,
    "x-app-key" : API_KEY
}

params = {
    "query": str(input("Tell me which exercises you did:")),
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

response = requests.post(url = excercise_endpoints, json=params, headers = headers_nutrition)
data = response.json()

print(data)

# # format waktu
# today = datetime.now()
# date = today.strftime("%d/%m/%Y")
# time = today.strftime("%H:%M:%S")

# excercise_type = (data["exercises"][0]["name"])
# duration_min = (data["exercises"][0]["duration_min"])
# calories = (data["exercises"][0]["nf_calories"])

# # menulis update ke sheet
# sheety_API_endpoint = os.getenv("sheety_API_endpoint")

# for x in range(len(data["exercises"])):
#     sheety_params = {
#         "workout" : {
#             "date": date,
#             "time": time,
#             "exercise": data["exercises"][x]["name"].title(),
#             "duration": data["exercises"][x]["duration_min"],
#             "calories" : data["exercises"][x]["nf_calories"]
#         }
#     }

# headers_sheety = {
#     "Authorization": f"Bearer {os.getenv('sheety_token_bearer')}"
# }

# add_row_response = requests.post(url = sheety_API_endpoint, json = sheety_params, headers=headers_sheety)
# print(add_row_response.json())