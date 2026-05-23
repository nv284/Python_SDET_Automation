from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time

# =====================================
# Mock OTP API Function
# =====================================

def get_otp_from_api(mobile_number):

    """
    Simulating OTP retrieval from API
    Real projects use:
    - REST API
    - Database
    - Email/SMS gateway
    """

    print(f"Fetching OTP for: {mobile_number}")

    # Mock OTP
    return "123456"

# =====================================
# Launch Browser
# =====================================

driver = webdriver.Chrome()

driver.maximize_window()

wait = WebDriverWait(driver, 10)

# =====================================
# Open Website
# =====================================

driver.get(
    "https://opensource-demo.orangehrmlive.com/"
)

# =====================================
# Step 1: Username
# =====================================

username = wait.until(
    EC.visibility_of_element_located(
        (By.NAME, "username")
    )
)

username.send_keys("Admin")

# =====================================
# Step 2: Password
# =====================================

password = driver.find_element(
    By.NAME,
    "password"
)

password.send_keys("admin123")

# =====================================
# Step 3: Login Button
# =====================================

login_btn = driver.find_element(
    By.XPATH,
    "//button[@type='submit']"
)

login_btn.click()

print("Login button clicked")

# =====================================
# Simulated OTP Flow
# =====================================

# In real applications:
# After login, OTP screen appears

print("OTP Verification Page Opened")

mobile_number = "9876543210"

# =====================================
# Fetch OTP from API
# =====================================

otp = get_otp_from_api(mobile_number)

print("OTP Received:", otp)

# =====================================
# Simulate OTP Entry
# =====================================

# Example only:
# Assume OTP field exists

print("Entering OTP...")

# Example:
# driver.find_element(By.ID, "otp").send_keys(otp)

# =====================================
# Simulate OTP Verification
# =====================================

print("OTP Verified Successfully")

# =====================================
# Validation
# =====================================

dashboard = wait.until(
    EC.visibility_of_element_located(
        (By.XPATH, "//h6[text()='Dashboard']")
    )
)

print("Dashboard Displayed")

# =====================================
# Wait and Close
# =====================================

time.sleep(5)

driver.quit()