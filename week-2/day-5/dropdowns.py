# Import required libraries
from selenium import webdriver
from selenium.webdriver.common.by import By

# Import Select class
from selenium.webdriver.support.ui import Select

import time

# Open browser
driver = webdriver.Chrome()

# Open website
driver.get("https://demoqa.com/select-menu")

# Maximize browser
driver.maximize_window()

# Wait for page load
time.sleep(2)

# ---------------- HANDLE DROPDOWN ----------------

# Find old style dropdown
dropdown = driver.find_element(By.ID, "oldSelectMenu")

# Create Select object
select = Select(dropdown)

# Select option using visible text
select.select_by_visible_text("Purple")

# Print selected option
print("Selected Color:", select.first_selected_option.text)

# Wait to see result
time.sleep(2)

# Close browser
driver.quit()