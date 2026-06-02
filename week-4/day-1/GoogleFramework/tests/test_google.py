import unittest

from config.config import URL, SEARCH_TEXT
from pages.google_page import GooglePage
from utilities.browser_utils import BrowserUtils

class TestGoogle(unittest.TestCase):

    def setUp(self):

        self.driver = BrowserUtils.get_driver()

        self.driver.get(URL)

    def test_google_search(self):

        page = GooglePage(self.driver)

        page.search(SEARCH_TEXT)

        self.assertIn(
            "Google",
            self.driver.title
        )

    def tearDown(self):

        self.driver.quit()

if __name__ == "__main__":
    unittest.main()

