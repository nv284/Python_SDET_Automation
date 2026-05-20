from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Launch Chrome browser
driver = webdriver.Chrome()

# Open website
driver.get("https://testautomationpractice.blogspot.com/")

# Maximize browser
driver.maximize_window()

time.sleep(2)

# ======================================================
# 1. contains() → Partial attribute matching
# ======================================================

name_field = driver.find_element(
    By.XPATH,
    "//input[contains(@id,'name')]"
)

name_field.send_keys("Nikhil")

print("contains() XPath executed")


# ======================================================
# 2. starts-with() → Match beginning of attribute
# ======================================================

email_field = driver.find_element(
    By.XPATH,
    "//input[starts-with(@id,'email')]"
)

email_field.send_keys("test@gmail.com")

print("starts-with() XPath executed")


# ======================================================
# 3. text() → Exact visible text match
# ======================================================

wiki_link = driver.find_element(
    By.XPATH,
    "//a[text()='GUI Elements']"
)

print("Exact text matched:", wiki_link.text)


# ======================================================
# 4. normalize-space()
# Removes unnecessary spaces
# ======================================================

header = driver.find_element(
    By.XPATH,
    "//h2[normalize-space()='Automation Testing Practice']"
)

print("normalize-space() executed:", header.text)


# ======================================================
# 5. parent axis
# Move one level upward
# ======================================================

parent_element = driver.find_element(
    By.XPATH,
    "//input[@id='name']/parent::div"
)#//input: Finds any <input> element on the page.[@id='name']: 
#Filters for the ID matching "name".
# /: Steps to the next connected element.
# parent::div: Moves up one level to the container <div>.
#<div class="form-group">  <!-- THIS IS TARGETED -->
 #   <label>Full Name</label>
 #   <input type="text" id="name" placeholder="Enter name">
#</div>


print("Parent axis executed")


# ======================================================
# 6. ancestor axis
# ancestor::: Searches all levels upward in the HTML tree structure.
# form: Limits the search specifically to <form> tags.
# ======================================================

ancestor_element = driver.find_element(
    By.XPATH,
  #  "//input[@id='email']/ancestor::form"
    //p[contains(text(), 'Section 1')]/ancestor::div[@class='widget-content']
)

print("Ancestor axis executed")


# ======================================================
# 7. child axis
# /: Steps down exactly one level in the HTML tree structure.
# child::h2: Restricts the search specifically to an <h2> tag at that next level.
# ======================================================

child_element = driver.find_element(
    By.XPATH,
    "//div[@class='widget-content']/child::h2"
)

print("Child axis executed")


# ======================================================
# 8. descendant axis
# /: Steps into the inner structure of the current element.
# descendant::input: Searches all lower levels (children, grandchildren, etc.) for <input> tags
# ======================================================

descendant_element = driver.find_element(
    By.XPATH,
   " //div[@id='Wikipedia1']/descendant::input[@class='wikipedia-search-button']"
  #  "//div[@class='widget-content']/descendant::input[@id='name']"
)

print("Descendant axis executed")


# ======================================================
# 9. following-sibling axis
# Locate next sibling element
# ======================================================

following_sibling = driver.find_element(
    By.XPATH,
    "//label[text()='Name:']/following-sibling::input"
)

print("Following sibling axis executed")


# ======================================================
# 10. preceding-sibling axis
# Locate previous sibling element
# ======================================================

preceding_sibling = driver.find_element(
    By.XPATH,
    "//input[@id='email']/preceding-sibling::label"
)

print("Preceding sibling axis executed")


# ======================================================
# 11. Dynamic XPath Example
# Handling changing attributes dynamically
# ======================================================

dynamic_xpath = driver.find_element(
    By.XPATH,
    "//input[contains(@class,'form-control')]"
)

print("Dynamic XPath executed")


# ======================================================
# Relative XPath Example
# Preferred over Absolute XPath
# ======================================================

phone_field = driver.find_element(
    By.XPATH,
    "//input[@id='phone']"
)

phone_field.send_keys("9876543210")

print("Relative XPath executed")


time.sleep(5)

# Close browser
driver.quit()