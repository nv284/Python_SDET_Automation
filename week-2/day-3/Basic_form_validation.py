from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# 1. Open the browser with basic stability flags
options = webdriver.ChromeOptions()
options.add_argument("--no-sandbox")
driver = webdriver.Chrome(options=options)

try:
    # 2. Go to the web form page
    driver.get("https://www.selenium.dev/selenium/web/web-form.html")
    
    # Create a reliable wait engine (waits up to 10 seconds)
    wait = WebDriverWait(driver, 10)
    
    print("--- Starting Form Validation Tests ---")

    # -------------------------------------------------------------
    # TEST 1: Validate the "Disabled Input" Field
    # -------------------------------------------------------------
    # Locate the disabled text field using its name attribute
    disabled_field = wait.until(EC.presence_of_element_located((By.NAME, "my-disabled")))
    
    # Validation A: Ensure it is physically displayed on screen
    assert disabled_field.is_displayed() == True, "Error: Disabled field is missing!"
    print(" Validation Passed: Disabled field is visible.")
    
    # Validation B: Confirm the user CANNOT interact with it
    assert disabled_field.is_enabled() == False, "Error: Field should be greyed out/disabled!"
    print(" Validation Passed: Field is correctly disabled.")

    # -------------------------------------------------------------
    # TEST 2: Validate the "Readonly Input" Field
    # -------------------------------------------------------------
    # Locate the readonly text field
    readonly_field = wait.until(EC.presence_of_element_located((By.NAME, "my-readonly")))
    
    # Validation A: Ensure it is enabled (you can click it, but you shouldn't be able to type)
    assert readonly_field.is_enabled() == True, "Error: Readonly field should be clickable."
    
    # Validation B: Verify the HTML 'readonly' structural attribute exists
    # If the attribute exists in HTML, get_attribute() returns the string "true"
    assert readonly_field.get_attribute("readonly") == "true", "Error: Missing HTML readonly property!"
    print(" Validation Passed: Readonly attribute verified successfully.")

except AssertionError as e:
    print(f" Validation failed: {e}")
except Exception as error:
    print(f" Unexpected browser error occurred: {error}")

finally:
    # 3. Safely kill browser threads
    driver.quit()
