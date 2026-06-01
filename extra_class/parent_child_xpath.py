from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.flipkart.com")

search_box = driver.find_element(
    By.XPATH,
    "//form//input[@title='Search for Products, Brands and More']"
)

search_box.send_keys("iPhone 15")


search = driver.find_element(
    By.XPATH,
    "//input[starts-with(@title,'Search')]"
)

search.send_keys("iPhone 15")

pro = driver.find_element(
    By.XPATH,"//div[contains(text(),'Apple iPhone 15')]"
    "/following-sibling::div"
    "//span[starts-with(@id,'productRating')]"
)
print(pro.text)