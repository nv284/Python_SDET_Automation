# Import required libraries
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

#Open website-->Switch to iframe-->Read text inside frame-->Switch back to main page

driver = webdriver.Chrome()


driver.get("https://demoqa.com/frames")


driver.maximize_window()

# Wait for page load
time.sleep(2)

# ---------------- SWITCH TO FRAME ----------------

# Switch to iframe using frame ID
driver.switch_to.frame("frame1")

# ---------------- ACCESS ELEMENT INSIDE FRAME ----------------

# Capture heading text inside frame
heading = driver.find_element(By.ID, "sampleHeading")

# Print frame text
print("Text Inside Frame:")
print(heading.text)

# ---------------- SWITCH BACK TO MAIN PAGE ----------------

driver.switch_to.default_content()

print(" Switched back to main webpage")

# Close browser
driver.quit()