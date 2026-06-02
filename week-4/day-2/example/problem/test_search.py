import unittest
from selenium import webdriver

class TestSearch(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_search(self):
        self.driver.get("https://www.google.com")
        self.assertIn("Google", self.driver.title)

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
