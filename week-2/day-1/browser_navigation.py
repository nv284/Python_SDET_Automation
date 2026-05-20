from selenium import webdriver
import time

# Launch Chrome browser
driver = webdriver.Chrome()

# Maximize browser window
driver.maximize_window()

# Open application
driver.get("https://www.google.com")

# Wait for 3 seconds
time.sleep(3)

# Close browser
driver.quit()