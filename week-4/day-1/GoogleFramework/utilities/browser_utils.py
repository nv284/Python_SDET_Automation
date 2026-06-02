from selenium import webdriver

class BrowserUtils:

    @staticmethod
    def get_driver():
        driver = webdriver.Chrome()
        driver.maximize_window()
        return driver
