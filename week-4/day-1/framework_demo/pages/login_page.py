from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class LoginPage(BasePage):
    #  Resilient attributes on the Swag Labs login window
    USERNAME_INPUT = (By.CSS_SELECTOR, "input[data-test='username']")
    PASSWORD_INPUT = (By.CSS_SELECTOR, "input[data-test='password']")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "input[data-test='login-button']")
    ERROR_CONTAINER = (By.CSS_SELECTOR, "h3[data-test='error']")

    def login_with_credentials(self, username, password):
        self.enter_text(self.USERNAME_INPUT, username)
        self.enter_text(self.PASSWORD_INPUT, password)
        self.click_element(self.LOGIN_BUTTON)

    def get_error_message(self):
        return self.find_element(self.ERROR_CONTAINER).text
