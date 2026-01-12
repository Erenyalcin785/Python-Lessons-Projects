from instabilgi import kullanici_adi,sifre
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()

url = "https://www.instagram.com/accounts/login/"

driver.get(url)
time.sleep(2)

ka =driver.find_element("xpath","//*[@id='loginForm']/div[1]/div[1]/div/label/input")
ka.send_keys(kullanici_adi)

sif = driver.find_element("xpath","//*[@id='loginForm']/div[1]/div[2]/div/label/input")
sif.send_keys(sifre)
sif.send_keys(Keys.ENTER)
time.sleep(2)
driver.maximize_window()


#ka2 = driver.find_element("xpath","//*[@id='loginForm']/div[1]/div[1]/div/label/input")
#ka2.send_keys(kullanici_adi)

#sif2 =driver.find_element("xpath","//*[@id='loginForm']/div[1]/div[2]/div/label/input")
#sif2.send_keys(sifre)
#sif2.send_keys(Keys.ENTER)
time.sleep(100)