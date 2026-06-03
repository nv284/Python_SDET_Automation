from selenium import webdriver
from selenium.webdriver.common.by import By

def test_hard_assert(driver):
    driver.get("https://opensource-demo.orangehrmlive.com")

    assert "OrangeHRM" in driver.title, "Title does not contain 'OrangeHRM'"
    username= driver.find_element(By.ID, "txtUsername")

    assert username.is_displayed(), "Username field is not displayed"
    
    dashboard = driver.find_element(By.XPATH, "//div[@id='dashboard']")

    assert dashboard.text == "Dashboard", "Dashboard text does not match expected value"