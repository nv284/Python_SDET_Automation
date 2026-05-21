# Import required Selenium libraries
#####  will stabilize the script by:

#Using Explicit Wait
#Avoiding time.sleep()
#Using proper locators
#Validating successful login
from selenium import webdriver
from selenium.webdriver.common.by import By

# Explicit wait imports
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# ---------------- START BROWSER ----------------

driver = webdriver.Chrome()

# Open website
driver.get("https://www.saucedemo.com/")

# Maximize browser
driver.maximize_window()

# ---------------- CREATE EXPLICIT WAIT ----------------

wait = WebDriverWait(driver, 10)

# ---------------- HANDLE USERNAME FIELD ----------------

username = wait.until(
    EC.visibility_of_element_located(
        (By.ID, "user-name")
    )
)

username.send_keys("standard_user")

# ---------------- HANDLE PASSWORD FIELD ----------------

password = wait.until(
    EC.visibility_of_element_located(
        (By.ID, "password")
    )
)

password.send_keys("secret_sauce")

# ---------------- HANDLE LOGIN BUTTON ----------------

login_button = wait.until(
    EC.element_to_be_clickable(
        (By.ID, "login-button")
    )
)

login_button.click()

# ---------------- VALIDATION ----------------

products_title = wait.until(
    EC.visibility_of_element_located(
        (By.CLASS_NAME, "title")
    )
)

print(" Automation Script Stabilized Successfully")
print("Page Heading:", products_title.text)

# ---------------- CLOSE BROWSER ----------------

driver.quit()

#| Stability Technique      | Used |
#| ------------------------ | ---- |
#| Explicit Wait            | ✅    |
#| Reliable Locators        | ✅    |
#| No Hardcoded Sleep       | ✅    |
#| Dynamic Element Handling | ✅    |
#| Validation Check         | ✅    |
