from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Launch Chrome browser
driver = webdriver.Chrome()

# Open website
driver.get("https://testautomationpractice.blogspot.com/")

# Maximize browser window
driver.maximize_window()

time.sleep(2)

# =========================================================
# 1. #id → Select element using ID
# Syntax:
# #idname
# =========================================================

# HTML Example:
# <input id="name">

name_field = driver.find_element(
    By.CSS_SELECTOR,
    "#name"
)

name_field.send_keys("Nikhil")

print("ID Selector Executed")


# =========================================================
# 2. .class → Select using class name
# Syntax:
# .classname
# =========================================================

# HTML Example:
# <div class="widget-content">

class_element = driver.find_element(
    By.CSS_SELECTOR,
    ".widget-content"
)

print("Class Selector Executed")


# =========================================================
# 3. tag.class → Tag with class
# Syntax:
# tagname.classname
# =========================================================

# HTML Example:
# <input class="form-control">

tag_class = driver.find_element(
    By.CSS_SELECTOR,
    "input.form-control"
)

print("Tag with Class Selector Executed")


# =========================================================
# 4. [attribute='value']
# Exact attribute matching
# =========================================================

# HTML Example:
# <input type="text">

exact_match = driver.find_element(
    By.CSS_SELECTOR,
    "input[type='text']"
)

print("Exact Attribute Match Executed")


# =========================================================
# 5. ^= → Starts with
# Matches beginning of attribute value
# =========================================================

# HTML Example:
# <input id="email123">

starts_with = driver.find_element(
    By.CSS_SELECTOR,
    "input[id^='em']"
)

print("Starts-With Selector Executed")


# =========================================================
# 6. $= → Ends with
# Matches ending of attribute value
# =========================================================

# HTML Example:
# <input id="user_email">

ends_with = driver.find_element(
    By.CSS_SELECTOR,
    "input[id$='ail']"
)

print("Ends-With Selector Executed")


# =========================================================
# 7. *= → Contains
# Matches partial attribute value
# =========================================================

# HTML Example:
# <input id="phone_number">

contains_selector = driver.find_element(
    By.CSS_SELECTOR,
    "input[id*='pho']"
)

print("Contains Selector Executed")


# =========================================================
# 8. > → Direct child selector
# Select only direct child
# =========================================================

# HTML Structure:
# <div class="widget-content">
#     <h2>Automation Testing Practice</h2>
# </div>

direct_child = driver.find_element(
    By.CSS_SELECTOR,
    "div.widget-content > h2"
)

print("Direct Child Selector Executed")


# =========================================================
# 9. + → Adjacent sibling selector
# Select immediate next sibling
# =========================================================

# Example Structure:
# <label>Name</label>
# <input id="name">

adjacent_sibling = driver.find_element(
    By.CSS_SELECTOR,
    "label + input"
)

print("Adjacent Sibling Selector Executed")


# =========================================================
# 10. ~ → General sibling selector
# Select all matching siblings after element
#~: The CSS general sibling combinator
# =========================================================

# Example Structure:
# <h2></h2>
# <p></p>
# <input>

general_sibling = driver.find_element(
    By.CSS_SELECTOR,
    "h2 ~ input"
)

print("General Sibling Selector Executed")


# =========================================================
# 11. :nth-child()
# Select element by position
# =========================================================

# Example:
# table tr: Finds row elements (<tr>) that live inside a <table>.
# :nth-child(2): Filters the list to target exactly the second item in that sequence.

nth_child = driver.find_element(
    By.CSS_SELECTOR,
    "table tr:nth-child(2)"
)

print("Nth Child Selector Executed")


# Wait before closing
time.sleep(5)

# Close browser
driver.quit()