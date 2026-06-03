from selenium.webdriver.common.by import By

class GooglePage:

    search_box = (By.NAME, "q")

    def __init__(self, driver):
        self.driver = driver

    def search(self, text):

        self.driver.find_element(
            *self.search_box
        ).send_keys(text)
