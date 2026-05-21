# Import required libraries
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

# Launch Chrome browser
driver = webdriver.Chrome()

# Maximize browser window
driver.maximize_window()

# Open practice website
driver.get("https://testautomationpractice.blogspot.com/")

# Wait for page load
time.sleep(2)

# =========================================
# TEXTBOX HANDLING
# =========================================

# Enter Name
driver.find_element(By.ID, "name").send_keys("John Doe")

# Enter Email
driver.find_element(By.ID, "email").send_keys("john@test.com")

# Enter Phone
driver.find_element(By.ID, "phone").send_keys("9876543210")

# Enter Address
driver.find_element(By.ID, "textarea").send_keys("Bangalore Karnataka")

# =========================================
# RADIO BUTTON HANDLING
# =========================================

# Select Male radio button
driver.find_element(By.ID, "male").click()

# =========================================
# CHECKBOX HANDLING
# =========================================

# Select Sunday checkbox
driver.find_element(By.ID, "sunday").click()

# Select Monday checkbox
driver.find_element(By.ID, "monday").click()

# =========================================
# SINGLE DROPDOWN HANDLING
# =========================================

# Country dropdown
country_dropdown = Select(driver.find_element(By.ID, "country"))

# Select by visible text
country_dropdown.select_by_visible_text("India")

# =========================================
# MULTI-SELECT DROPDOWN HANDLING
# =========================================

# Colors dropdown
colors_dropdown = Select(driver.find_element(By.ID, "colors"))

# Select multiple options
colors_dropdown.select_by_visible_text("Red")
colors_dropdown.select_by_visible_text("Blue")
colors_dropdown.select_by_visible_text("Green")

# =========================================
# CHECKBOX VALIDATION
# =========================================

# Check if checkbox is selected
sunday_checkbox = driver.find_element(By.ID, "sunday")

if sunday_checkbox.is_selected():
    print("Sunday checkbox is selected")
else:
    print("Sunday checkbox is NOT selected")

# =========================================
# RADIO BUTTON VALIDATION
# =========================================

male_radio = driver.find_element(By.ID, "male")

if male_radio.is_selected():
    print("Male radio button selected")

# =========================================
# GET SELECTED DROPDOWN VALUE
# =========================================

selected_country = country_dropdown.first_selected_option.text

print("Selected country is:", selected_country)

# =========================================
# WAIT TO SEE RESULT
# =========================================

time.sleep(5)

# Close browser
driver.quit()