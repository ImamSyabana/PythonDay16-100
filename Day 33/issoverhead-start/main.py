import requests
from datetime import datetime
import smtplib
import time

MY_LAT = -6.259095 # Your latitude
MY_LONG = 107.118509 # Your longitude

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()

iss_latitude = float(data["iss_position"]["latitude"])
iss_longitude = float(data["iss_position"]["longitude"])

#Your position is within +5 or -5 degrees of the ISS position.


parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise_UTC_hour = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset_UTC_hour = int(data["results"]["sunset"].split("T")[1].split(":")[0])

sunrise_minute = int(data["results"]["sunrise"].split("T")[1].split(":")[1])
sunset_minute = int(data["results"]["sunset"].split("T")[1].split(":")[1])

sunrise_WIB_hour = (sunrise_UTC_hour + 7) % 24
sunset_WIB_hour = (sunset_UTC_hour + 7) % 24

time_now = datetime.now()

my_curr_loc = (MY_LAT, MY_LONG)
iss_curr_loc = (iss_latitude, iss_longitude)

# print(data["results"]["sunrise"])
# print(sunset_WIB_hour)
# print(sunset_minute)
# print(time_now.hour)

while True:
    time.sleep(60)
    if (abs(iss_curr_loc[0] - my_curr_loc[0]) <= 5 and abs(iss_curr_loc[1] - my_curr_loc[1]) <= 5) and (time_now.hour > sunset_WIB_hour or time_now.hour < sunrise_WIB_hour):
        my_email = "expensivebonlap@gmail.com"
        my_password = "otlcxftlknqbeype"
        
        with smtplib.SMTP("smtp.gmail.com", 587) as connection:
            connection.starttls() #TLS : transport layer security
            connection.login(user = my_email, password = my_password)
            connection.sendmail(from_addr = my_email, 
                                to_addrs="imamsyabana046@gmail.com", 
                                msg=f"ISS Notification\n\nLook UP there is an ISS crossing")
#If the ISS is close to my current position
# and it is currently dark
# Then send me an email to tell me to look up.
# BONUS: run the code every 60 seconds.



