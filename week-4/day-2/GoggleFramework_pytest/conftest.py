# conftest.py

import pytest

from config.config import URL
from utilities.browser_utils import BrowserUtils

@pytest.fixture
def browser():

    driver = BrowserUtils.get_driver()

    driver.get(URL)

    yield driver

    driver.quit()
