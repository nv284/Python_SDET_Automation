# Import required libraries
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://demoqa.com/alerts")

# Maximize browser
driver.maximize_window()

# ---------------- CLICK ALERT BUTTON ----------------

# Click button that opens alert
driver.find_element(By.ID, "alertButton").click()

# Wait to see alert
time.sleep(2)

# ---------------- HANDLE ALERT ----------------

# Switch to alert popup
alert = driver.switch_to.alert

# Capture alert text
alert_text = alert.text


print("Alert Message:", alert_text)

# Accept alert (Click OK)
alert.accept()

# Print success message
print(" Alert handled successfully")
driver.quit()