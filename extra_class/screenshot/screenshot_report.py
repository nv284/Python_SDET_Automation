from selenium import webdriver
from datetime import datetime

# Create report file
report = open("TestReport.txt", "w")

driver = webdriver.Chrome()

try:
    # Open website
    driver.get("https://www.google.com")

    # Verify title
    expected_title = "Google"
    actual_title = driver.title

    if actual_title == expected_title:
        report.write("TEST CASE: Google Title Verification\n")
        report.write("STATUS: PASS\n")
        report.write(f"ACTUAL TITLE: {actual_title}\n")

    else:
        raise Exception("Title Mismatch")

except Exception as e:

    # Take Screenshot
    screenshot_name = "FailureScreenshot.png"
    driver.save_screenshot(screenshot_name)

    report.write("TEST CASE: Google Title Verification\n")
    report.write("STATUS: FAIL\n")
    report.write(f"ERROR: {e}\n")
    report.write(f"SCREENSHOT: {screenshot_name}\n")

finally:
    report.close()
    driver.quit()

print("Execution Completed")