from selenium import webdriver
from selenium.webdriver.common.by import By
from datetime import datetime
from selenium.webdriver.common.keys import Keys


# keep Chrome browser open after program finishes
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://en.wikipedia.org/wiki/Main_Page")

# click anchor tag berdasarkan css selector 
num_articles = driver.find_element(By.XPATH, value='//*[@id="articlecount"]/ul/li[2]/a[1]')
num_articles.click()

# #menemukan element menggunakan link text
# all_portals = driver.find_element(By.LINK_TEXT, value = "Most viewed pages")
# all_portals.click()

# mengetikkan ke search box
search = driver.find_element(By.CSS_SELECTOR, value = "#p-search .cdx-button span")
search.click()

# # mengirim input keyboard ke selenium
search_text = driver.find_element(By.CSS_SELECTOR, value = ".cdx-text-input__input")
search_text.send_keys("Python")

# # menekan enter kepada ketikan yang sudah dimasukkan 
send_search = driver.find_element(By.CSS_SELECTOR, value = ".cdx-search-input .cdx-search-input__end-button")
send_search.send_keys(Keys.ENTER)
