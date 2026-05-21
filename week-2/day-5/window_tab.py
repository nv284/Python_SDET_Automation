#| Scenario         | Example            |
#| ---------------- | ------------------ |
#| Payment gateway  | Opens new tab      |
#| OAuth login      | Google login popup |
#| Report download  | Opens new window   |
#| External website | Opens new tab      |
####################################################################
# Import required libraries
# Import required libraries
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# ---------------- START BROWSER ----------------

driver = webdriver.Chrome()

# Open Python website
driver.get("https://www.python.org/")

# Maximize browser
driver.maximize_window()

# Wait for page load
time.sleep(2)

# ---------------- STORE MAIN WINDOW ----------------

main_window = driver.current_window_handle

print("Main Window ID:")
print(main_window)

# ---------------- GET DOWNLOADS PAGE URL ----------------

downloads_link = driver.find_element(By.LINK_TEXT, "Downloads")

downloads_url = downloads_link.get_attribute("href")

# ---------------- OPEN NEW TAB ----------------

driver.execute_script(f"window.open('{downloads_url}', '_blank');")

# Wait for new tab
time.sleep(2)

# ---------------- GET ALL WINDOW IDS ----------------

all_windows = driver.window_handles

print("All Window IDs:")
print(all_windows)

# ---------------- SWITCH TO NEW TAB ----------------

for window in all_windows:

    if window != main_window:

        driver.switch_to.window(window)

        print("✅ Switched to New Tab")

        # Print page title
        print("New Tab Title:")
        print(driver.title)

# ---------------- SWITCH BACK TO MAIN TAB ----------------

driver.switch_to.window(main_window)

print("✅ Switched Back to Main Tab")

print("Main Page Title:")
print(driver.title)

# ---------------- CLOSE BROWSER ----------------

driver.quit()