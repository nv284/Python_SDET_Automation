from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

# Open login page
driver.get("https://the-internet.herokuapp.com/login")

# Test data
username = "tomsmith"
password = "SuperSecretPassword!"

# Enter credentials
driver.find_element(By.ID, "username").send_keys(username)
driver.find_element(By.ID, "password").send_keys(password)
driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

# UI Validation
actual_message = driver.find_element(By.ID, "flash").text

# Python Validation (Business Logic)
expected_text = "You logged into a secure area!"

# Hybrid Validation
assert expected_text in actual_message

print("Hybrid validation passed")

driver.quit()