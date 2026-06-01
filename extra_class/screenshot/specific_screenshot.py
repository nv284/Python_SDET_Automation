from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

driver.get("https://the-internet.herokuapp.com/login")

time.sleep(2)

# Find Login button
login_btn = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")

# Capture button screenshot
login_btn.screenshot("login_button.png")

print("Button screenshot captured")

driver.quit()