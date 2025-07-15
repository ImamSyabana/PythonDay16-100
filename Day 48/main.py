from selenium import webdriver
from selenium.webdriver.common.by import By

# keep Chrome browser open after program finishes
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.amazon.com/dp/B075CYMYK6?ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6&th=1")

# mencari berdasarkan nama class
price_dollar = driver.find_element(By.CSS_SELECTOR, value=".a-price-whole")
price_cents = driver.find_element(By.CLASS_NAME, value="a-price-fraction")
print(f"The price is {price_dollar.text}.{price_cents.text}")

# mencari element berdasarkan nama 
driver.get("https://www.python.org/")
search_bar = driver.find_element(By.NAME, value = "q")
print(search_bar.tag_name)
print(search_bar.get_attribute("placeholder "))

# mencari berdasarkan id 
button = driver.find_element(By.ID, value = "submit")
print(button.size)

# mencari element menggunakan sistem css selector
docs_link = driver.find_element(By.CSS_SELECTOR, value = ".documentation-widget a")
print(docs_link.text)

# mencari element menggunakanan Xpath
submitBug = driver.find_element(By.XPATH, value = '//*[@id="site-map"]/div[2]/div/ul/li[3]/a')
print(submitBug.text)

# mencari BANYAK element menggunakan find_elements
driver.find_elements(By.XPATH, value = '//*[@id="site-map"]/div[2]/div/ul/li[3]/a')

# # kalo mau nutup chrome 
# driver.close() # nutup satu tab
driver.quit() # menutup keseluruhan chrome 

