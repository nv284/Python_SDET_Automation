from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Launch Chrome Browser
driver = webdriver.Chrome()

# Maximize window
driver.maximize_window()

# Open Google
driver.get("https://www.google.com")

# Find search box
search_box = driver.find_element(By.NAME, "q")

# Enter text
search_box.send_keys("Python Selenium")

# Press Enter
search_box.send_keys(Keys.ENTER)

# Wait for results to load
time.sleep(3)

# Take screenshot
driver.save_screenshot("google_search_result.png")

print("Screenshot captured successfully!")

# Close browser
driver.quit()