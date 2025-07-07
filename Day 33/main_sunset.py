import requests
from datetime import datetime

MY_LAT = -6.259095
MY_LONG = 107.118509

parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted" : 0,
}

response = requests.get("https://api.sunrise-sunset.org/json", params= parameters)
response.raise_for_status()

data = response.json()

sunrise = data["results"]["sunrise"]
sunset = (data["results"]["sunset"]).split("T")[1].split(":")[0]

print(sunrise)
print(sunrise.split("T")[1].split(":")[1])

time_now = datetime.now()
print(time_now.hour)