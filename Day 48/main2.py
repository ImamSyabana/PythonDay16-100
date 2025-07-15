from selenium import webdriver
from selenium.webdriver.common.by import By
from datetime import datetime

# keep Chrome browser open after program finishes
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.python.org/")


# mencari element menggunakan sistem css selector
eventName_list = []
eventName = driver.find_elements(By.CSS_SELECTOR, value= ".event-widget .menu a")
for name in eventName:
    #print(name.text)
    eventName_list.append(name.text)


eventDate_list = []
eventDate = driver.find_elements(By.CSS_SELECTOR, value = ".event-widget .menu time")
for date in eventDate:
    date_text = date.get_attribute("datetime")  # e.g., "2024-07-22"

    # Parse the string into a datetime object
    # The .fromisoformat() method is perfect for this format
    dt_object = datetime.fromisoformat(date_text)

    # Get just the date part and convert it to a string
    date_only_string = dt_object.strftime('%Y-%m-%d')
    #print(date_only_string)
    eventDate_list.append(date_only_string)

print(eventName_list)
print(eventDate_list)

event_dict = {}

for x in range(len(eventName_list)):
    event_dict[x] = {
        "time" : f"{eventDate_list[x]}", "name" : f"{eventName_list[x]}"
        }
    
print(event_dict)
# # kalo mau nutup chrome 
# driver.close() # nutup satu tab
driver.quit() # menutup keseluruhan chrome 