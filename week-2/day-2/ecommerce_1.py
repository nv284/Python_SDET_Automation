from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

driver.get("file:///D:/ecommerce.html")

driver.maximize_window()

# -------------------------------
# LOGIN SECTION
# -------------------------------

driver.find_element(
    By.ID,
    "email"
).send_keys("admin@test.com")

driver.find_element(
    By.XPATH,
    "//input[starts-with(@id,'pwd_')]"
).send_keys("12345")

driver.find_element(
    By.CSS_SELECTOR,
    "[class*='login']"
).click()

time.sleep(2)

# -------------------------------
# CLICK ADD TO CART FOR iPhone
# -------------------------------

driver.find_element(
    By.XPATH,
    "//td[text()='iPhone 15']/following-sibling::td/following-sibling::td/button"
).click()

time.sleep(2)

# -------------------------------
# VALIDATE SUCCESS MESSAGE
# -------------------------------

message = driver.find_element(
    By.CLASS_NAME,
    "success-msg"
)

print("Message:", message.text)

# -------------------------------
# CLICK HOME PAGE LINK
# -------------------------------

driver.find_element(
    By.PARTIAL_LINK_TEXT,
    "Home"
).click()

time.sleep(3)

driver.quit()