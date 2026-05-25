from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# 1. Open the Chrome browser session
driver = webdriver.Chrome()

try:
    # 2. Navigate to Sauce Demo -> Triggers HTTP GET (Read)
    driver.get("https://saucedemo.com")
    
    # 3. Locate the text input boxes
    username_field = driver.find_element(By.ID, "user-name")
    password_field = driver.find_element(By.ID, "password")
    
    # 4. Fill in the valid user credentials
    username_field.send_keys("standard_user")
    password_field.send_keys("secret_sauce")
    
    # 5. Click the Login button -> Triggers HTTP POST (Create/Process)
    login_button = driver.find_element(By.ID, "login-button")
    login_button.click()
    
    # Small buffer pause to let the web layout resolve
    time.sleep(5)
    
    # 6. QA Verification: Assert you successfully reached the inventory dashboard
    assert "inventory.html" in driver.current_url
    print("QA Test Result: PASSED  - Successfully logged into Sauce Demo.")

except AssertionError:
    print("QA Test Result: FAILED  - Did not navigate to the product page.")

finally:
    # 7. Safe teardown of the automated browser window
    driver.quit()
