import requests
from selenium import webdriver
import time

# -----------------------------
# DELETE API Request
# -----------------------------

user_id = 2

url = f"https://reqres.in/api/users/{user_id}"

response = requests.delete(url)

print("Status Code:", response.status_code)

# -----------------------------
# API Validation
# -----------------------------

assert response.status_code == 201, \
    "User deletion failed"

print("User deleted successfully.")

# -----------------------------
# Selenium Validation
# -----------------------------

driver = webdriver.Chrome()

driver.maximize_window()

driver.get("https://reqres.in")

print("Website Title:", driver.title)

assert "Reqres" in driver.title

print("Website verification passed.")

time.sleep(3)

driver.quit()

print("Test Execution Completed")