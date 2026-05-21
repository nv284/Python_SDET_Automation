# Import required libraries
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Launch Chrome browser
driver = webdriver.Chrome()

# ---------------- IMPLICIT WAIT ----------------
# Selenium will wait up to 10 seconds
# before throwing an exception

driver.implicitly_wait(10)


driver.get("https://www.saucedemo.com/")

# Maximize browser
driver.maximize_window()

# ---------------- LOGIN ----------------


driver.find_element(By.ID, "user-name").send_keys("standard_user")


driver.find_element(By.ID, "password").send_keys("secret_sauce")


driver.find_element(By.ID, "login-button").click()

# ---------------- VALIDATION ----------------

# Get page title after login
title = driver.title


print("Page Title is:", title)

# Check login success
if "Swag Labs" in title:
    print(" Login Successful")
else:
    print(" Login Failed")

# Wait to see result
time.sleep(3)

# Close browser
driver.quit()