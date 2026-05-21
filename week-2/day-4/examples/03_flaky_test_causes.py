# Import required libraries
from tkinter import Button

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://demoqa.com/dynamic-properties")
driver.maximize_window()

# BAD PRACTICE
# Wait only 2 seconds
time.sleep(2)

# Find dynamic button
button = driver.find_element(By.ID, "enableAfter")

# Try clicking button
button.click()
print("Button clicked successfully")

driver.quit()
###########################################
##Sometimes:
#Button enables quickly → PASS
#Sometimes:
#Button still disabled → FAIL 
#####################################################

################  FIX CODE WITH EXPLICIT WAIT  ####################
#####################################################
# Import required libraries
from selenium import webdriver
from selenium.webdriver.common.by import By

# Explicit wait imports
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Launch browser
driver = webdriver.Chrome()

# Open website
driver.get("https://demoqa.com/dynamic-properties")

# Maximize browser
driver.maximize_window()

# Create explicit wait
wait = WebDriverWait(driver, 10)

# Wait until button becomes clickable
button = wait.until(
    EC.element_to_be_clickable(
        (By.ID, "enableAfter")
    )
)


button.click()

# Print success message
print(" Button clicked successfully")
print(" Flaky issue resolved")

driver.quit()

#############################################
#Explicit Wait:

#Waits dynamically
#Checks button state continuously
#Clicks only when button becomes clickable