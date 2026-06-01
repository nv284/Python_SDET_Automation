import random
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Generate unique user
username = f"user_{random.randint(1000,9999)}"
password = "Test123"

# ---------------------------
# Step 1: Create User via API
# ---------------------------
payload = {
    "username": username,
    "password": password
}

response = requests.post(
    "https://api.demoblaze.com/signup",
    json=payload
)

print(f"User created: {username}")

# ---------------------------
# Step 2: Login via UI
# ---------------------------
driver = webdriver.Chrome()
wait = WebDriverWait(driver, 10)

try:
    driver.get("https://www.demoblaze.com")

    # Click Login
    driver.find_element(By.ID, "login2").click()

    # Enter credentials
    wait.until(
        EC.visibility_of_element_located((By.ID, "loginusername"))
    ).send_keys(username)

    driver.find_element(By.ID, "loginpassword").send_keys(password)

    driver.find_element(
        By.XPATH,
        "//button[text()='Log in']"
    ).click()

    # ---------------------------
    # Step 3: UI Validation
    # ---------------------------
    welcome = wait.until(
        EC.visibility_of_element_located((By.ID, "nameofuser"))
    )

    ui_username = welcome.text.replace("Welcome ", "")

    # ---------------------------
    # Step 4: Hybrid Validation
    # ---------------------------
    assert ui_username == username

    print("Hybrid Validation Passed")
    print(f"API User : {username}")
    print(f"UI User  : {ui_username}")

finally:
    driver.quit()