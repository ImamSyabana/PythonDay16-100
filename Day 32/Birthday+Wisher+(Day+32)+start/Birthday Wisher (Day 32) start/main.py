import smtplib

my_email = "expensivebonlap@gmail.com"
my_password = "otlcxftlknqbeype"


with smtplib.SMTP("smtp.gmail.com", 587) as connection:
    connection.starttls() #TLS : transport layer security
    connection.login(user = my_email, password = my_password)
    connection.sendmail(from_addr = my_email, 
                        to_addrs="imamsyabana046@gmail.com", 
                        msg="Subject:Hello\n\nThis is the body of the email.")
