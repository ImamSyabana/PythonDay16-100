from bs4 import BeautifulSoup
import requests
from datetime import datetime
import string
import smtplib
import time

import os
from dotenv import find_dotenv, load_dotenv


URL = "https://appbrewery.github.io/Zillow-Clone/"

headers = {
    "Accept-Language": "en-GB,en;q=0.9,ja-JP;q=0.8,ja;q=0.7,en-US;q=0.6",
    "user-agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36"
}

response = requests.get(URL, headers=headers)

raw_web_page = response.text #mengeluarkan html beserta semua tag2 nya
raw_web_page

soup = BeautifulSoup(raw_web_page, "html.parser") #membuat object untuk parsing html


# mencari list alamat apartment
apartment_adress = soup.find_all(name="address")
address_list = [(adress.getText()).strip() for adress in apartment_adress]



# mencari price list apartment
apartment_price = soup.find_all(name = "span", class_="PropertyCardWrapper__StyledPriceLine")
price_list = [(price.getText()).strip() for price in apartment_price]
#print(price_list)
import re
# Use a list comprehension and a regular expression to find the pattern
price_list = [re.search(r'\$[\d,]+', s).group(0) for s in price_list]
#print(price_list)



# mengambil link masing masing iklan apartment
apartment_links = soup.find_all(name = "a", class_ = "property-card-link")
links_list = [link.get("href") for link in apartment_links]
#print(links_list)


## Membuat selenium program untuk input data secara otomatis

from selenium import webdriver
from selenium.webdriver.common.by import By
from datetime import datetime
from selenium.webdriver.common.keys import Keys

# keep Chrome browser open after program finishes
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://docs.google.com/forms/d/e/1FAIpQLScCMXaZJmx86dNjkrDZW5cwi9juKdV5hvuQmCfUi9z4-kp1wQ/viewform")


for x in range(len(address_list)):
    # 1. ngisi kolom adress yang mau diisi
    time.sleep(0.1)
    adress_col = driver.find_element(By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
    adress_col.click()
    adress_col.send_keys(address_list[x])
    time.sleep(0.1)

    #2. ngisi kolom price per month
    price_col = driver.find_element(By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
    price_col.click()
    price_col.send_keys(price_list[x])
    time.sleep(0.1)

    #3. ngisi kolom link iklan apartment
    ads_col = driver.find_element(By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
    ads_col.click()
    ads_col.send_keys(links_list[x])
    time.sleep(0.1)

    #4. submit response
    submit_btn = driver.find_element(By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div')
    submit_btn.click()
    time.sleep(0.1)

    #5. submit another response
    repeat = driver.find_element(By.XPATH, value='/html/body/div[1]/div[2]/div[1]/div/div[4]/a')
    repeat.click()