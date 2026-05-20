## Python Syntax Examples

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()

# Basic Interaction
search_box = driver.find_element(By.NAME, "q")
search_box.clear()
search_box.send_keys("Automation Testing")
search_box.submit()

# Advanced Interaction (Hover)
menu = driver.find_element(By.ID, "menu-hover")
actions = ActionChains(driver)
actions.move_to_element(menu).perform()