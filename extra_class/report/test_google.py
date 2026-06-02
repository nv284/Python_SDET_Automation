#pip install selenium
#pip install pytest
#pip install pytest-html

# run the test with the command: pytest test_google.py --html=report.html

from selenium import webdriver

def test_google_title():

    driver = webdriver.Chrome()

    driver.get("https://www.google.com")

    assert driver.title == "Google"

    driver.quit()