from selenium import webdriver

driver = webdriver.Chrome()

try:
    driver.get("https://www.google.com")

    # Intentional failure
    assert "Facebook" in driver.title

except Exception as e:
    print("Test Failed")
    driver.save_screenshot("failure_screenshot.png")

finally:
    driver.quit()