from xbilgi import kullanici_adi,sifre
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()

url ="https://x.com/?lang=tr"

driver.get(url)

giris = driver.find_element("xpath","//*[@id='react-root']/div/div/div[2]/main/div/div/div[1]/div/div/div[3]/div[4]/a/div")
giris.click()
time.sleep(2)

ka = driver.find_element("xpath","//*[@id='layers']/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[4]/label/div/div[2]/div/input")
ka.send_keys(kullanici_adi)
time.sleep(5)
ka.send_keys(Keys.ENTER)
time.sleep(2)

ka2 = driver.find_element("xpath","//*[@id='layers']/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[4]/label/div/div[2]/div/input")
ka2.send_keys(kullanici_adi)
ka2.send_keys(Keys.ENTER)
time.sleep(2)

sif = driver.find_element("xpath","//*[@id='layers']/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input")
sif.send_keys(sifre)
sif.send_keys(Keys.ENTER)
time.sleep(100)