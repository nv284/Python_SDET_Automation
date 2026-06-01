from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()

driver.get("https://www.flipkart.com")
driver.maximize_window()

# Close login popup
try:
    driver.find_element(By.XPATH, "//span[text()='✕']").click()
except:
    pass

# Search iPhone 15
search_box = driver.find_element(
    By.XPATH,
    "//input[@title='Search for Products, Brands and More']"
)

search_box.send_keys("iPhone 15")
search_box.send_keys(Keys.ENTER)

time.sleep(5)

# Parent -> Child XPath
iphone = driver.find_element(
    By.XPATH,
    "//div[@data-id]//div[contains(text(),'Apple iPhone 15')]"
)

print("Product Found:", iphone.text)

# Price using sibling xpath
#price = driver.find_element(
#   By.XPATH,
#   "//div[contains(text(),'Apple iPhone 15')]"
#   "/following-sibling::*[contains(text(),'₹')]"
#)
#print("Price:", price.text)


# find rating 
rating = driver.find_element(
    By.XPATH , "//div[contains(text(),'Apple iPhone 15')]"
    "/following-sibling::div"
    "//div[contains(@class, 'MKiFS6')]"
)
print( "Rating :", rating.text)

rating1= driver.find_element(
    By.XPATH ,"//div[contains(text(),'Apple iPhone 15')]"
    "/following-sibling::div[@class = 'a7saXW']"
    "//child::div[contains(text(), '4.6')]"
 
)
print("Rating 1:", rating1.text)










driver.quit()