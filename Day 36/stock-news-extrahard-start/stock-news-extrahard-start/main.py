import requests
import json
import smtplib
from email.message import EmailMessage

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").



STOCK_API = "EJV3S15R1DL8FSI6"

stockAPI_parameters = {
    "function" : "TIME_SERIES_DAILY",
    "symbol" : STOCK,
    "outputsize":"compact",
    "apikey" : STOCK_API
    
}

response_stock_api = requests.get("https://www.alphavantage.co/query?", params=stockAPI_parameters)
response_stock_api.raise_for_status()

data = response_stock_api.json()

#print(data["Time Series (Daily)"])

close_stock_data = [float(value["4. close"]) for tgl, value in data["Time Series (Daily)"].items()]



# # BUAT SEMENTARA KALO KENA LIMIT MAKE API ALPHAVANTAGE
# close_stock_data = [293.94, 315.35, 315.65, 300.71, 317.66, 323.63, 325.78, 327.55, 340.47, 348.68, 322.16, 322.05, 316.35, 329.13, 325.31, 319.11, 326.43, 326.09, 308.58, 295.14, 284.7, 332.05, 344.27, 342.69, 346.46, 358.43, 356.9, 362.89, 339.34, 341.04, 334.62, 343.82, 342.09, 349.98, 342.82, 347.68, 334.07, 318.38, 298.26, 284.82, 276.22, 275.35, 280.26, 287.21, 280.52, 282.16, 292.03, 285.88, 284.95, 259.51, 250.74, 237.97, 227.5, 241.37, 241.55, 254.11, 252.35, 252.31, 252.4, 272.2, 221.86, 233.29, 239.43, 267.28, 282.76, 268.46, 259.16, 263.55, 273.13, 272.06, 288.14, 278.39, 248.71, 236.26, 235.86, 225.31, 238.01, 249.98, 240.68, 248.09, 230.58, 222.15, 262.67, 263.45, 279.1, 272.04, 284.65, 292.98, 281.95, 290.8, 302.8, 330.53, 337.8, 354.4, 360.56, 354.11, 355.84, 355.94, 336.51, 328.5]

#print(close_stock_data)


## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 
def get_news():
    NEWS_API = "3d530014c1994f019f4287bab37aa778"

    newsAPI_parameters = {
        "q": COMPANY_NAME,
        "searchIn" : "description",
        #"domains": ("eg bbc.co.uk", "techcrunch.com", "engadget.com"),
        "from": "2025-06-08",
        "to": "2025-07-08",
        #"language": "en",
        "sortBy" : "popularity",
        "pageSize" : "10",
        "apiKey": NEWS_API
    }
    response_news_api = requests.get("https://newsapi.org/v2/top-headlines?", params=newsAPI_parameters)
    response_news_api.raise_for_status()

    data = response_news_api.json()

    news_message = ""

    for articles in data['articles'][:3]:
        news_message = news_message + f"[NEWS TITLE] : {articles['title']} \n\n [NEWS CONTENT] {articles['description']} \n [READ MORE] : {articles['url']} \n\n\n\n"

    return str(news_message)
## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number. 

def send_mail():
    # send an email
    my_email = 'expensivebonlap@gmail.com'
    my_password = 'otlcxftlknqbeype'

    msg = EmailMessage()
    msg['Subject'] = 'Stock Price Notification'
    msg['From'] = my_email
    msg['To'] = 'imamsyabana046@gmail.com'
    msg.set_content(get_news())  # Automatically handles UTF-8 encoding

    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=my_password)
        connection.send_message(msg)
        
        
# kirim email kalo perubahan harga lebih dari 5%
if (abs(close_stock_data[-1] - close_stock_data[-2])) / close_stock_data[-2] > 0.05:
    send_mail()
else:
    print("harga saham tidak berubah lebih dari 5%")
    

#Optional: Format the SMS message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

