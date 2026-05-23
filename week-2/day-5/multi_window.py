from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time

# =====================================
# Step 1: Launch Browser
# =====================================

driver = webdriver.Chrome()

driver.maximize_window()

wait = WebDriverWait(driver, 10)

# =====================================
# Step 2: Open Website
# =====================================

driver.get(
    "https://demoqa.com/browser-windows"
)

print("Website Opened")

# =====================================
# Step 3: Store Parent Window
# =====================================

parent_window = driver.current_window_handle

print("Parent Window ID:")
print(parent_window)

# =====================================
# Step 4: Open New Tab
# =====================================

new_tab_button = wait.until(
    EC.element_to_be_clickable(
        (By.ID, "tabButton")
    )
)

new_tab_button.click()

print("New Tab Opened")

# =====================================
# Step 5: Get All Windows
# =====================================

all_windows = driver.window_handles

print("All Window Handles:")
print(all_windows)

# =====================================
# Step 6: Switch to Child Window
# =====================================

for window in all_windows:

    if window != parent_window:

        driver.switch_to.window(window)

        print("Switched to Child Window")

        break

# =====================================
# Step 7: Validate Child Window Content
# =====================================

message = wait.until(
    EC.visibility_of_element_located(
        (By.ID, "sampleHeading")
    )
)

print("Child Window Text:")
print(message.text)

# =====================================
# Step 8: Close Child Window
# =====================================

driver.close()

print("Child Window Closed")

# =====================================
# Step 9: Switch Back to Parent Window
# =====================================

driver.switch_to.window(parent_window)

print("Returned to Parent Window")

# =====================================
# Step 10: Validate Parent Window
# =====================================

page_title = driver.title

print("Parent Page Title:")
print(page_title)

# =====================================
# Step 11: Wait and Close Browser
# =====================================

time.sleep(5)

driver.quit()