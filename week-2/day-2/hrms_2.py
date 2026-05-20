from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

driver.get("file:///D:/hrms.html")

driver.maximize_window()

# --------------------------------
# LOGIN
# --------------------------------

driver.find_element(
    By.ID,
    "user_name"
).send_keys("admin")

driver.find_element(
    By.XPATH,
    "//input[starts-with(@id,'pass_')]"
).send_keys("admin123")

driver.find_element(
    By.CSS_SELECTOR,
    "[class*='login']"
).click()

time.sleep(2)

# --------------------------------
# SEARCH EMPLOYEE
# --------------------------------

driver.find_element(
    By.CSS_SELECTOR,
    "[id^='search_']"
).send_keys("Rahul")

time.sleep(2)

# --------------------------------
# CLICK EDIT FOR RAHUL
# --------------------------------

driver.find_element(
    By.XPATH,
    "//td[text()='Rahul']/following-sibling::td/following-sibling::td/following-sibling::td/button[1]"
).click()

time.sleep(2)

# --------------------------------
# GET ENTIRE ROW
# --------------------------------

row = driver.find_element(
    By.XPATH,
    "//td[text()='Rahul']/parent::tr"
)

print("Employee Row:", row.text)

# --------------------------------
# VALIDATE STATUS
# --------------------------------

status = driver.find_element(
    By.XPATH,
    "//td[text()='Rahul']/following-sibling::td[2]"
)

print("Status:", status.text)

time.sleep(3)

driver.quit()