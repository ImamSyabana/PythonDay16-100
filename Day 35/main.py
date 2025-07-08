import requests
import smtplib

import os
from dotenv import find_dotenv, load_dotenv

# mencari lokasi file .env secara otomatis 
dotenv_path = find_dotenv()

# load the entries as environtment variables
load_dotenv(dotenv_path)

# stored the env variables within a python variable
API_KEY = os.getenv("API_KEY")

# mendapat latitude longitut
parameters = {
    "lat":-6.259037,
    "lon":107.118540,
    "cnt": 4,
    "appid": API_KEY
}

# membuat request ke API forecast
response = requests.get("https://api.openweathermap.org/data/2.5/forecast?", params = parameters)
response.raise_for_status()

# print the http status code
#print(response.status_code)

#print response ke console
weather_data = response.json()
print(weather_data)

weather_pred_list = []
weather_pred_dict = {}

for x in range(4):
    weather_pred_dict["id"] = weather_data["list"][x]["weather"][0]["id"]
    weather_pred_dict["main"] = weather_data["list"][x]["weather"][0]["main"]
    weather_pred_dict["description"] = weather_data["list"][x]["weather"][0]["description"]
    
    weather_pred_list.append(weather_pred_dict)

#print(weather_pred_list)

message = ""
for x in range(len(weather_pred_list)):
    message = message + (f"{weather_pred_list[x]["main"]} class {weather_pred_list[x]["id"]} ({weather_pred_list[x]["description"]}) is expected over the next {(x + 1) * 3} hours.\n")

# send an email
my_email = "expensivebonlap@gmail.com"
my_password = "otlcxftlknqbeype"

with smtplib.SMTP("smtp.gmail.com", 587) as connection:
    connection.starttls() #TLS : transport layer security
    connection.login(user = my_email, password = my_password)
    connection.sendmail(from_addr = my_email, 
                        to_addrs='imamsyabana046@gmail.com', 
                        msg=f"Subject:Weather Info\n\n{message}")


# # send an email
# if any(code < 700 for code in weather_pred_list):
#     my_email = "expensivebonlap@gmail.com"
#     my_password = "otlcxftlknqbeype"
    
#     with smtplib.SMTP("smtp.gmail.com", 587) as connection:
#         connection.starttls() #TLS : transport layer security
#         connection.login(user = my_email, password = my_password)
#         connection.sendmail(from_addr = my_email, 
#                             to_addrs='imamsyabana046@gmail.com', 
#                             msg=f"Subject:Weather Info\n\nRain is coming bring an umbrella")
    
# elif all(code >= 700 for code in weather_pred_list):
#     my_email = "expensivebonlap@gmail.com"
#     my_password = "otlcxftlknqbeype"
    
#     with smtplib.SMTP("smtp.gmail.com", 587) as connection:
#         connection.starttls() #TLS : transport layer security
#         connection.login(user = my_email, password = my_password)
#         connection.sendmail(from_addr = my_email, 
#                             to_addrs='imamsyabana046@gmail.com', 
#                             msg=f"Subject:Weather Info\n\nNo rain expected")


#print(type(weather_data["list"][1]["weather"][0]["id"]))