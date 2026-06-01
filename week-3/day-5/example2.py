from selenium import webdriver
from selenium.webdriver.common.by import By
import requests

# Step 1: Generate token (Backend Validation)
response = requests.post(
    "https://dummyjson.com/auth/login",
    json={
        "username": "emilys",
        "password": "emilyspass"
    }
)

token = response.json().get("accessToken")
print(f"Generated Token: {token}")

# Python Validation
assert token is not None
print("Token generated successfully")

# Step 2: Open UI
driver = webdriver.Chrome()

driver.get("https://the-internet.herokuapp.com/login")

# Login through UI
driver.find_element(By.ID, "username").send_keys("tomsmith")
driver.find_element(By.ID, "password").send_keys("SuperSecretPassword!")
driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

# Step 3: UI Validation
message = driver.find_element(By.ID, "flash").text
print(f"UI Message: {message}")

# Hybrid Validation
if token:
    assert "You logged into a secure area!" in message
    print("Hybrid validation passed")

driver.quit()