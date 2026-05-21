# Import required libraries
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Launch Chrome browser
driver = webdriver.Chrome()

# Open SauceDemo website
driver.get("https://www.saucedemo.com/")

# Maximize browser
driver.maximize_window()

# Wait for page load
time.sleep(2)

# ---------------- NEGATIVE TEST DATA ----------------
invalid_username = "wrong_user"
invalid_password = "wrong_pass"

# ---------------- FIND USERNAME FIELD ----------------
username = driver.find_element(By.ID, "user-name")

# Enter invalid username
username.send_keys(invalid_username)

# ---------------- FIND PASSWORD FIELD ----------------
password = driver.find_element(By.ID, "password")

# Enter invalid password
password.send_keys(invalid_password)

# ---------------- CLICK LOGIN BUTTON ----------------
login_button = driver.find_element(By.ID, "login-button")
login_button.click()

# Wait for response
time.sleep(2)

# ---------------- VALIDATION ----------------
# Capture error message
error_message = driver.find_element(By.CSS_SELECTOR, "h3[data-test='error']").text

# Check if error message is displayed
if "Username and password do not match" in error_message:
    print("Negative Test Passed")
    print("Error message displayed correctly")
else:
    print(" Negative Test Failed")

# Close browser
driver.quit()