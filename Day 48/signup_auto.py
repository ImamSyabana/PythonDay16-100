
from selenium import webdriver
from selenium.webdriver.common.by import By
from datetime import datetime
from selenium.webdriver.common.keys import Keys


# keep Chrome browser open after program finishes
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://secure-retreat-92358.herokuapp.com/")

firstName_input = driver.find_element(By.NAME, value="fName")
firstName_input.send_keys("Zelkova")

lastName_input = driver.find_element(By.NAME, value="lName")
lastName_input.send_keys("Prunus")

mail_input = driver.find_element(By.NAME, value="email")
mail_input.send_keys("charmander@gmail.com")

sign_button= driver.find_element(By.XPATH, value= '/html/body/form/button')
sign_button.send_keys(Keys.ENTER)

