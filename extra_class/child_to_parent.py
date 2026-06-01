from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.flipkart.com")

iphone = driver.find_element(
    By.XPATH,
    "//div[contains(text(),'Apple iPhone 15')]"
)

# child - to parent 
parent = driver.find_element(
    By.XPATH,
    "//div[contains(text(),'Apple iPhone 15')]/parent::div"
)

print(parent.text)

#grandchildren
product = driver.find_element(
    By.XPATH,
    "//div[@data-id]/div/div[contains(text(),'Apple iPhone 15')]"
)

print(product.text)

#floowing sibling 
price = driver.find_element(
    By.XPATH,
    "//div[contains(text(),'Apple iPhone 15')]"
    "/following-sibling::div[contains(text(),'₹')]"
)

print(price.text)
#Preceding Sibling
rating = driver.find_element(
    By.XPATH,
    "//div[contains(text(),'₹')]"
    "/preceding-sibling::div[1]"
)

print(rating.text)

#ancestor

card = driver.find_element(
    By.XPATH,
    "//div[contains(text(),'Apple iPhone 15')]"
    "/ancestor::div[@data-id]"
)

print(card.text)

#ancestor+siblin 
next_product = driver.find_element(
    By.XPATH,
    "//div[contains(text(),'Apple iPhone 15')]"
    "/ancestor::div[@data-id]"
    "/following-sibling::div[1]"
)

print(next_product.text)

#Parent → Child → Grandchild → Ancestor (Complex)

product = driver.find_element(
    By.XPATH,
    "//div[@data-id]"
    "/div/div[contains(text(),'Apple iPhone 15')]"
    "/ancestor::div[@data-id]"
)

print(product.text)