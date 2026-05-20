from selenium import webdriver
from selenium.webdriver.common.by import By
import time


driver = webdriver.Chrome()

driver.get("login.html")

driver.maximize_window()

driver.find_element(By.ID, "username").send_keys("admin")

driver.find_element(By.ID, "password").send_keys("1234")

driver.find_element(By.ID, "loginBtn").click()

time.sleep(2)

message = driver.find_element(By.ID, "message").text

print(message)

driver.quit()
