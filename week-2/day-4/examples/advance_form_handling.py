from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Launch browser
driver = webdriver.Chrome()

# Open website
driver.get("https://demoqa.com/automation-practice-form")

# Maximize window
driver.maximize_window()

wait = WebDriverWait(driver, 15)

# ==========================
# Step 1: Text Field Handling
# ==========================

driver.find_element(By.ID, "firstName").send_keys("John")
driver.find_element(By.ID, "lastName").send_keys("Doe")
driver.find_element(By.ID, "userEmail").send_keys("john@example.com")

# ==========================
# Step 2: Radio Button Handling
# ==========================

gender = driver.find_element(By.XPATH, "//label[text()='Male']")
gender.click()

# ==========================
# Step 3: Mobile Number
# ==========================

driver.find_element(By.ID, "userNumber").send_keys("9876543210")

# ==========================
# Step 4: Date Picker Handling
# ==========================

date_input = driver.find_element(By.ID, "dateOfBirthInput")

# Select all existing date
date_input.send_keys(Keys.CONTROL + "a")

# Enter new date
date_input.send_keys("15 Aug 1998")
date_input.send_keys(Keys.ENTER)

# ==========================
# Step 5: Dynamic Subject Field
# ==========================

subjects = driver.find_element(By.ID, "subjectsInput")

subjects.send_keys("Maths")
subjects.send_keys(Keys.ENTER)

subjects.send_keys("Physics")
subjects.send_keys(Keys.ENTER)

# ==========================
# Step 6: Checkbox Handling
# ==========================

driver.find_element(By.XPATH, "//label[text()='Sports']").click()

# ==========================
# Step 7: File Upload
# ==========================

upload = driver.find_element(By.ID, "uploadPicture")

# Change file path as per your system
upload.send_keys(r"week-2\day-4\examples\download.png")

# ==========================
# Step 8: Address Handling
# ==========================

driver.find_element(By.ID, "currentAddress").send_keys(
    "Bangalore, Karnataka"
)

# ==========================
# Step 9: Dynamic Dropdown Handling
# ==========================

# State Dropdown
state = driver.find_element(By.ID, "react-select-3-input")
state.send_keys("NCR")
state.send_keys(Keys.ENTER)

# City Dropdown
city = driver.find_element(By.ID, "react-select-4-input")
city.send_keys("Delhi")
city.send_keys(Keys.ENTER)

# ==========================
# Step 10: Multi-Step Form Submission
# ==========================

submit_btn = driver.find_element(By.ID, "submit")

# Scroll to submit button
driver.execute_script("arguments[0].scrollIntoView();", submit_btn)

time.sleep(2)

submit_btn.click()

# ==========================
# Step 11: Validation
# ==========================

confirmation = wait.until(
    EC.visibility_of_element_located(
        (By.ID, "example-modal-sizes-title-lg")
    )
)

print("Form Submitted Successfully")
print("Popup Message:", confirmation.text)

# Wait for 5 seconds
time.sleep(5)

# Close browser
driver.quit()