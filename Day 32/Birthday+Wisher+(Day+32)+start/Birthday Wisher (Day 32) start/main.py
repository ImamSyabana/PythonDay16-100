# import smtplib

# my_email = "expensivebonlap@gmail.com"
# my_password = "otlcxftlknqbeype"


# with smtplib.SMTP("smtp.gmail.com", 587) as connection:
#     connection.starttls() #TLS : transport layer security
#     connection.login(user = my_email, password = my_password)
#     connection.sendmail(from_addr = my_email, 
#                         to_addrs="imamsyabana046@gmail.com", 
#                         msg="Subject:Hello\n\nThis is the body of the email.")

import datetime as dt

now = dt.datetime.now()
year = now.year
month = now.month
day_of_the_week = now.weekday()
if year == 2020:
    print("WEAR a face mask")
print(day_of_the_week)

date_of_birth = dt.datetime(year = 2002, month = 10 , day =12, hour = 16)
print(date_of_birth)