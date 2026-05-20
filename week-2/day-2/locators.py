from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.find_element(By.NAME, "password")

driver.find_element(By.CLASS_NAME, "success-msg")

driver.find_elements(By.TAG_NAME, "img")

driver.find_element(By.LINK_TEXT, "Google Search")

driver.find_element(By.PARTIAL_LINK_TEXT, "Watch")

driver.find_element(By.XPATH, "//input[@id='email']")

driver.find_element(
By.XPATH,
"//button[contains(@class,'primary')]"
)  ##contains is used when we want to find an element with a partial match of the attribute value

driver.find_element(
By.XPATH,
"//input[starts-with(@id,'user_')]"
)  ##starts-with is used when we want to find an element with a partial match of the attribute value that starts with a specific string

driver.find_element(
By.XPATH,
"//button[text()='Login']"
) ##text() is used when we want to find an element with a specific text content

driver.find_element(
By.XPATH,
"//td[text()='John']/following-sibling::td[2]/button"
)##following-sibling is used to find an element that is a sibling of another element. In this case,
#we are finding the button that is the second sibling of the td element that contains the text 'John'

#### CSS selector 

driver.find_element(By.CSS_SELECTOR, "#email")

driver.find_element(By.CSS_SELECTOR, ".login-btn") #class selector 

driver.find_element(
By.CSS_SELECTOR,
"input[type='password']"
)# attribute selector 

driver.find_element(
By.CSS_SELECTOR,
"[class*='primary']"
)#* is used to find an element with a partial match of the attribute value

