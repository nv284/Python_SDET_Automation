#Why conftest.py?

#PyTest automatically loads fixtures from:
#no need to write -from conftest import browser
import pytest
from selenium import webdriver

@pytest.fixture
def browser():

    driver = webdriver.Chrome()

    yield driver

    driver.quit()
