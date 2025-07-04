# import smtplib

# my_email = "expensivebonlap@gmail.com"
# my_password = "otlcxftlknqbeype"


# with smtplib.SMTP("smtp.gmail.com", 587) as connection:
#     connection.starttls() #TLS : transport layer security
#     connection.login(user = my_email, password = my_password)
#     connection.sendmail(from_addr = my_email, 
#                         to_addrs="imamsyabana046@gmail.com", 
#                         msg="Subject:Hello\n\nThis is the body of the email.")

# import datetime as dt

# now = dt.datetime.now()
# year = now.year
# month = now.month
# day_of_the_week = now.weekday()
# if year == 2020:
#     print("WEAR a face mask")
# print(day_of_the_week)

# date_of_birth = dt.datetime(year = 2002, month = 10 , day =12, hour = 16)
# print(date_of_birth)

# use datetime modul to obtain thhe current day of the week 
import datetime as dt

day_list = ['Monday', 'Tuesday', 'Wednesday', 'Thursdat', 'Friday', 'Saturday', 'Sunday']

now = dt.datetime.now()
curr_day = now.weekday()

# open theh quotes.txt file to obtain a list of quotes
with open("Day 32/Birthday+Wisher+(Day+32)+start/Birthday Wisher (Day 32) start/quotes.txt", "r") as file:
    list_quotes = file.readlines()
    #print(len(list_quotes))
    
    
# Use the random module to pick a random quote from list of quotes
import random

randomPicked_quotes = random.choice(list_quotes)
print(randomPicked_quotes)

# Use the smtplib to send the email to yourself
import smtplib

my_email = "expensivebonlap@gmail.com"
my_password = "otlcxftlknqbeype"

scheduledMail_day = 'Friday'

if curr_day == day_list.index(scheduledMail_day):
    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls() #TLS : transport layer security
        connection.login(user = my_email, password = my_password)
        connection.sendmail(from_addr = my_email, 
                            to_addrs="imamsyabana046@gmail.com", 
                            msg=f"Subject:Quotes for today\n\n{randomPicked_quotes}")
