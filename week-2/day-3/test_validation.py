
from time import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

try:
    
    driver.get("https://selenium.dev")
    time.sleep(4)
    main_header = driver.find_element(By.TAG_NAME, "h1")
    
    assert "Selenium automates browsers" in main_header.text
    print(" Text validation passed! Found expected headline.")
    
   
    assert main_header.is_displayed() == True
    print(" Visibility validation passed! Header is visible on screen.")
    
    
    assert main_header.get_attribute("class") == "h1"
    print(" Attribute validation passed! Class name matches.")

except AssertionError:
    print(" One of the validations failed!")
except Exception as e:
    print(f" An error occurred (e.g., Element not found): {e}")

finally:
    # 5. Clean up and close the browser window
    driver.quit()
