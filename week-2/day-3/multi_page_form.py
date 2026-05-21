# =========================================
# IMPORT LIBRARIES
# =========================================

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

# =========================================
# LAUNCH BROWSER
# =========================================

driver = webdriver.Chrome()

driver.maximize_window()

# =========================================
# OPEN WEBSITE
# =========================================

driver.get("https://automationexercise.com/")

time.sleep(3)

# =========================================
# PAGE 1 -> GO TO LOGIN PAGE
# =========================================

driver.find_element(By.LINK_TEXT, "Signup / Login").click()

time.sleep(2)

# =========================================
# PAGE 2 -> SIGNUP FORM
# =========================================

# Enter Name
driver.find_element(By.NAME, "name").send_keys("John Doe")

# Enter Email
driver.find_element(By.XPATH, "//input[@data-qa='signup-email']").send_keys(
    "pohn12345@test.com"
)

# Click Signup button
driver.find_element(By.XPATH, "//button[text()='Signup']").click()

time.sleep(3)

# =========================================
# PAGE 3 -> ACCOUNT INFORMATION FORM
# =========================================

# -----------------------------
# RADIO BUTTON
# -----------------------------

# Select Mr radio button
driver.find_element(By.ID, "id_gender1").click()

# -----------------------------
# PASSWORD
# -----------------------------

driver.find_element(By.ID, "password").send_keys("Test@123")

# -----------------------------
# DROPDOWN HANDLING
# -----------------------------

# Day dropdown
day_dropdown = Select(driver.find_element(By.ID, "days"))
day_dropdown.select_by_visible_text("15")

# Month dropdown
month_dropdown = Select(driver.find_element(By.ID, "months"))
month_dropdown.select_by_visible_text("May")

# Year dropdown
year_dropdown = Select(driver.find_element(By.ID, "years"))
year_dropdown.select_by_visible_text("1998")

# -----------------------------
# CHECKBOX HANDLING
# -----------------------------

# Newsletter checkbox
driver.find_element(By.ID, "newsletter").click()

# Special offers checkbox
driver.find_element(By.ID, "optin").click()

# -----------------------------
# ADDRESS DETAILS
# -----------------------------

driver.find_element(By.ID, "first_name").send_keys("John")

driver.find_element(By.ID, "last_name").send_keys("Doe")

driver.find_element(By.ID, "company").send_keys("ABC Technologies")

driver.find_element(By.ID, "address1").send_keys("Bangalore Karnataka")

# Country dropdown
country_dropdown = Select(driver.find_element(By.ID, "country"))
country_dropdown.select_by_visible_text("India")

driver.find_element(By.ID, "state").send_keys("Karnataka")

driver.find_element(By.ID, "city").send_keys("Bangalore")

driver.find_element(By.ID, "zipcode").send_keys("560001")

driver.find_element(By.ID, "mobile_number").send_keys("9876543210")

# =========================================
# VALIDATION EXAMPLES
# =========================================

newsletter_checkbox = driver.find_element(By.ID, "newsletter")

if newsletter_checkbox.is_selected():
    print("Newsletter checkbox selected")

gender_radio = driver.find_element(By.ID, "id_gender1")

if gender_radio.is_selected():
    print("Male radio button selected")

# =========================================
# SUBMIT FORM
# =========================================

driver.find_element(By.XPATH, "//button[text()='Create Account']").click()

print("Account created successfully")

# =========================================
# WAIT TO SEE RESULT
# =========================================

time.sleep(5)

# Close browser
driver.quit()

#| Feature               | Selenium Method |
#| --------------------- | --------------- |
#| Multi-page navigation | `click()`       |
#| Textbox handling      | `send_keys()`   |
#| Radio button          | `click()`       |
#| Checkbox              | `click()`       |
#| Dropdown (`select`)   | `Select()`      |
#| Validation            | `is_selected()` |
#| Form submission       | `click()`       |
#------------------------------------------------------


#Homepage
#   ↓
#Click "Signup / Login"
#   ↓
#Browser opens Login Page
#   ↓
#Selenium continues execution there