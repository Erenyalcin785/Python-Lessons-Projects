from selenium import webdriver 
import time
driver = webdriver.Chrome() 
url = "https://www.reuters.com/" 
driver.get(url)
time.sleep(10)