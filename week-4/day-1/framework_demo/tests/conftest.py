import pytest
import json
from selenium import webdriver

@pytest.fixture(scope="session")
def config():
    with open("config.json") as config_file:
        return json.load(config_file)

@pytest.fixture()
def driver(config):
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    yield driver
    driver.quit()
