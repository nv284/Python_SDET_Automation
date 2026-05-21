import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

try:
    driver.get("https://python.org")
    time.sleep(5)

    search_filed = driver.find_element(By.NAME , "q")

    search_filed.clear()

    search_filed.send_keys("documentation")
    go_button = driver.find_element(By.ID , "submit")
    go_button.click()

    time.sleep(3)
    print("search excuted successfully!")

finally:
    driver.quit()
