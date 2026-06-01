from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

try:

    print("launching the browser")
    driver.get("https://www.google.com")
    print("navigating to google")

# breakpoint 
    print("Current URL:", driver.current_url)
    search_box = driver.find_element(By.NAME, "wrong_name")
    search_box.send_keys("Python Selenium")

except Exception as e:
    print("An error occurred:", e)
    #screenshot for debugging
    driver.save_screenshot("error_screenshot.png")

finally:
    print("Closing the browser")
    driver.quit()

