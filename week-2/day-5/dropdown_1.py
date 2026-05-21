# Import required libraries
from selenium import webdriver
from selenium.webdriver.common.by import By

# Import Select class
from selenium.webdriver.support.ui import Select

import time

# Launch browser
driver = webdriver.Chrome()

# Open website
driver.get("https://practice.expandtesting.com/dropdown")

# Maximize browser
driver.maximize_window()

# Wait for page load
time.sleep(2)

# ---------------- HANDLE DROPDOWN ----------------

# Find dropdown element
country_dropdown = driver.find_element(By.ID, "country")

# Create Select object
select = Select(country_dropdown)

# Select country using visible text
select.select_by_visible_text("India")

# Print selected country
print("Selected Country:", select.first_selected_option.text)

# Wait to see result
time.sleep(2)

# Close browser
driver.quit()