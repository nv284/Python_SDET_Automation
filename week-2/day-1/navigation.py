from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get("https://google.com")

time.sleep(20)
driver.get("https://youtube.com")
time.sleep(20)
driver.back()
#driver.forword()
time.sleep(20)
driver.quit()
