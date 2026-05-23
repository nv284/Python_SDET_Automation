# Step 1: Import advanced automation tools
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://saucedemo.com")


wait = WebDriverWait(driver, 10)


driver.find_element(By.ID, "user-name").send_keys("standard_user")
driver.find_element(By.ID, "password").send_keys("secret_sauce")
driver.find_element(By.ID, "login-button").click()

# Add two items to the cart
driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
driver.find_element(By.ID, "add-to-cart-sauce-labs-bike-light").click()

# Go to the shopping cart page
driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()


# Wait until ALL inventory items inside the cart are present and loaded
cart_items = wait.until(
    EC.presence_of_all_elements_located((By.CLASS_NAME, "cart_item"))
)
print(f" Step 1: Found all {len(cart_items)} inventory items loaded securely inside the cart.")

# Click Checkout to move to the form page
driver.find_element(By.ID, "checkout").click()

# Fill the information form
driver.find_element(By.ID, "first-name").send_keys("John")
driver.find_element(By.ID, "last-name").send_keys("Doe")
driver.find_element(By.ID, "postal-code").send_keys("12345")
driver.find_element(By.ID, "continue").click()


# Wait until the payment summary element shows the exact subtotal text
subtotal_ready = wait.until(
    EC.text_to_be_present_in_element((By.CLASS_NAME, "summary_subtotal_label"), "Item total: $39.98")
)
if subtotal_ready:
    print("💵 Step 2: Confirmed checkout subtotal text matches expected price values.")

# Click Finish to complete order
driver.find_element(By.ID, "finish").click()


# On the completion page, the cart badge number tracking icon must completely vanish/disappear.
cart_badge_gone = wait.until(
    EC.invisibility_of_element_located((By.CLASS_NAME, "shopping_cart_badge"))
)
if cart_badge_gone:
    print(" Step 3: Verified checkout completion. Cart quantity badge has vanished.")

# Step 4: Graceful shutdown
time.sleep(2)
driver.quit()
