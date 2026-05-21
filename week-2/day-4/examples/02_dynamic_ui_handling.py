# Import required Selenium libraries
#Open Python.org
#Wait for the search box dynamically
#Enter keyword "selenium"
#Click search button
#Wait for search results page
#Print first result
from selenium import webdriver
from selenium.webdriver.common.by import By

# Explicit wait imports
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# ---------------- START BROWSER ----------------


driver = webdriver.Chrome()


driver.get("https://www.python.org/")
driver.maximize_window()

# ---------------- CREATE EXPLICIT WAIT ----------------

wait = WebDriverWait(driver, 10)

# ---------------- HANDLE DYNAMIC SEARCH BOX ----------------

# Wait until search box becomes visible
search_box = wait.until(
    EC.visibility_of_element_located(
        (By.ID, "id-search-field")
    )
)

# Enter search keyword
search_box.send_keys("selenium")

# ---------------- HANDLE DYNAMIC SEARCH BUTTON ----------------

# Wait until search button becomes clickable
search_button = wait.until(
    EC.element_to_be_clickable(
        (By.ID, "submit")
    )
)

# Click search button
search_button.click()

# ---------------- WAIT FOR SEARCH RESULTS ----------------

# Wait until first result appears
first_result = wait.until(
    EC.visibility_of_element_located(
        (By.CSS_SELECTOR, ".list-recent-events li")
    )
)

# ---------------- PRINT RESULT ----------------

print(" Dynamic UI handled successfully")

print("First Search Result:")
print(first_result.text)

# ---------------- CLOSE BROWSER ----------------

driver.quit()