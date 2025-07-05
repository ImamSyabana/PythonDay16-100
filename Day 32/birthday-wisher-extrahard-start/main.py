##################### Extra Hard Starting Project ######################
import pandas as pd
import random
import smtplib
import datetime as dt
# 1. Update the birthdays.csv
df = pd.read_csv("Day 32/birthday-wisher-extrahard-start/birthdays.csv")
#print(df)

# Modify an existing row by its index label
df.loc[1] = ['Riria', 'imamsyabana046@gmail.com', 2002, 10, 8]
#print(df)

with open("Day 32/birthday-wisher-extrahard-start/birthdays.csv", "w", newline = '') as file:
    df.to_csv(file, index=False)
    
    
# 2. Check if today matches a birthday in the birthdays.csv
list_bday = pd.read_csv("Day 32/birthday-wisher-extrahard-start/birthdays.csv")
    
#print(int(list_bday.loc[1, ("month")]))


now = dt.datetime.now()
curr_day = now.day # check current day
curr_month = now.month # check current month

if curr_day == (list_bday.loc[1, ("day")]) and curr_month == (list_bday.loc[1, ("month")]):
    
# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
    picked_letter_idx = random.randint(1,3)
    with open((f"Day 32/birthday-wisher-extrahard-start/letter_templates/letter_{picked_letter_idx}.txt"), "r") as bday_letter:
        bday_origin = (bday_letter.read())
    with open((f"Day 32/birthday-wisher-extrahard-start/letter_templates/output_letter_{picked_letter_idx}.txt"), "w") as personalized_bday_letter:
        personalized_bday_letter.write((bday_origin.replace("[NAME]", (list_bday.loc[1, ("name")]))))
        
    with open((f"Day 32/birthday-wisher-extrahard-start/letter_templates/output_letter_{picked_letter_idx}.txt"), "r") as personalized_bday_letter:
        readytoSend_letter = (personalized_bday_letter.read())
        
        
        
# 4. Send the letter generated in step 3 to that person's email address.
        my_email = "expensivebonlap@gmail.com"
        my_password = "otlcxftlknqbeype"
        
        with smtplib.SMTP("smtp.gmail.com", 587) as connection:
            connection.starttls() #TLS : transport layer security
            connection.login(user = my_email, password = my_password)
            connection.sendmail(from_addr = my_email, 
                                to_addrs=list_bday.loc[1, ("email")], 
                                msg=f"Subject:Happy Birthday\n\n{readytoSend_letter}")
