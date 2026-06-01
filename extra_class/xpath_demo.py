from selenium import webdriver
from selenium.webdriver.common.by import By

#launching webdriver
driver = webdriver.Chrome()
driver.get("https://automationexercise.com/login")
username=driver.find_element(By.XPATH, "//input[@data-qa='login-email']")
username.send_keys("admin@test.com")
