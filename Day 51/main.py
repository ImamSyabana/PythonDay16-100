
from selenium import webdriver
from selenium.webdriver.common.by import By
from datetime import datetime
from selenium.webdriver.common.keys import Keys
import time

import os
from dotenv import find_dotenv, load_dotenv

# mencari lokasi file .env secara otomatis 
dotenv_path = find_dotenv()

# load the entries as environtment variables
load_dotenv(dotenv_path)


PROMISED_DOWN = 150
PROMISED_UP = 10
TWITTER_USERNAME = os.getenv("TWITTER_USERNAME")
TWITTER_PASSWORD = os.getenv("TWITTER_PASSWORD")

# keep Chrome browser open after program finishes
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver_path = webdriver.Chrome(options=chrome_options)

class InternetSpeedTwitterBot:
    def __init__(self):
        self.driver = driver_path
        self.down = PROMISED_DOWN
        self.up = PROMISED_UP
        
    def get_internet_speed(self):
        self.driver.get("https://www.speedtest.net/")
        startButton = self.driver.find_element(By.CLASS_NAME, value = "start-text")
        startButton.click()
        time.sleep(45)
        self.downSpeed = self.driver.find_element(By.XPATH, value='//*[@id="container"]/div[1]/div[3]/div/div/div/div[2]/div[2]/div/div[4]/div/div[3]/div/div/div[2]/div[1]/div[1]/div/div[2]/span')
        self.upSpeed = self.driver.find_element(By.XPATH, value='//*[@id="container"]/div[1]/div[3]/div/div/div/div[2]/div[2]/div/div[4]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span')
        self.downSpeed = float(self.downSpeed.text)
        self.upSpeed = float(self.upSpeed.text)
     
        
    def tweet_at_provider(self):

        self.driver.get("https://twitter.com/login")
        time.sleep(5)
        
        #fase login
        input_username = self.driver.find_element(By.CSS_SELECTOR, value='div div input')
        input_username.send_keys(TWITTER_USERNAME)
        time.sleep(5)
        next_button = self.driver.find_element(By.XPATH, value='//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/button[2]/div/span/span')
        next_button.click()
        time.sleep(5)
        input_pass = self.driver.find_element(By.XPATH, value='//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input')
        input_pass.send_keys(TWITTER_PASSWORD)
        login_click = self.driver.find_element(By.XPATH, value='//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div[1]/div/div/button/div/span/span')
        login_click.click()
        
        #buat postingan
        time.sleep(5)
        clickPost = self.driver.find_element(By.XPATH, value='//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div[2]/div[1]/div/div/div[1]/div[2]/div/div/div/div/div/div/div/div/div/div/div/div/div[1]/div/div/div/div/div/div[2]/div/div/div/div')
        clickPost.click()
        write_post = self.driver.find_element(By.XPATH, value='//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div[2]/div/div/div/div/div/div[1]/div/div/div/div/div/div[2]/div/div/div/div')
        
        #write_post.send_keys("dasdas")
        
        write_post.send_keys(f"Hey Biznet Provider, why is my internet speed {self.downSpeed}down/{self.upSpeed}up when I pay for {PROMISED_DOWN}down/{PROMISED_UP}up?")
        
        send_post = self.driver.find_element(By.XPATH, value='//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[2]/div[2]/div/div/div/button')
        send_post.click()
        
bot = InternetSpeedTwitterBot()
speed_retriever = bot.get_internet_speed()
tweet_sender = bot.tweet_at_provider()

