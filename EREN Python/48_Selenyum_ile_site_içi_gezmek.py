from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()

url = "https://www.dr.com.tr/?gclsrc=aw.ds&gad_source=1&gad_campaignid=20259104108&gbraid=0AAAAADsp1mfUSqpSy2yPEpfvEKJADEyDf&gclid=Cj0KCQiA9OnJBhD-ARIsAPV51xNFqOlXg5yIylf8ehMZbjLC3LwpVhC8irdLcnxtC5rJ6_lFWnD2qvUaArldEALw_wcB"

driver.get(url)
time.sleep(2)

driver.maximize_window()

kitap = driver.find_element("xpath","/html/body/div[2]/header/div[3]/div[3]/ul/li[1]/a")
kitap.click()
time.sleep(2)

kitapara = driver.find_element("css selector","body > div.site-container > header > div.site-header-center.bg-c255.py-10 > div > div > div.search.col-12.col-lg-7.mt-10.mt-lg-0.dr-flex > div.search-wrapper.col-12.col-lg-10.p-0 > input")
kitapara.send_keys("Şiir")
time.sleep(2)

kitapara.send_keys(Keys.ENTER)
time.sleep(3)


for i in range(1,10):

    bilgi = driver.find_element("xpath","/html/body/div[1]/div[3]/div/div/main/div[3]/div[1]/div[{}]/div/div[2]/h3[1]/a".format(i))

    print(bilgi.text)


#kitap1 =driver.find_element("xpath", "xpath","/html/body/div[1]/div[3]/div/div/main/div[3]/div[1]/div[1]/div/div[2]/h3[1]/a")
#kitap2 =driver.find_element("xpath", "xpath","/html/body/div[1]/div[3]/div/div/main/div[3]/div[1]/div[2]/div/div[2]/h3[1]/a")
#kitap3= driver.find_element("xpath", "xpath","/html/body/div[1]/div[3]/div/div/main/div[3]/div[1]/div[]/div/div[2]/h3[1]/a")

driver.close()
#/html/body/div[1]/div[3]/div/div/main/div[2]/div[1]/div[{}]/div/div[4]/h3[1]
#/html/body/div[1]/div[3]/div/div/main/div[2]/div[1]/div[{}]/div/div[4]/h3[1]/a