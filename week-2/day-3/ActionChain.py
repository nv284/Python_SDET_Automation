import time
from selenium import webdriver
from selenium.webdriver.common.by import By
# 1. Import the ActionChains tool for advanced interactions
from selenium.webdriver import ActionChains

driver = webdriver.Chrome()

try:
    
    driver.get("https://python.org")
    time.sleep(2) 
    community_menu= driver.find_element(By.LINK_TEXT , "Community")
    mouse_actions = ActionChains(driver)
    mouse_actions.move_to_element(community_menu)

    mouse_actions.perform()
    time.sleep(3)
    print("Hover action successful!")

finally:
    driver.quit()