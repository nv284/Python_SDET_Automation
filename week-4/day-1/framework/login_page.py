from selenium.webdriver.common.by import By

class LoginPage:

    USERNAME = (By.NAME, "username")

    PASSWORD = (By.NAME, "password")

    LOGIN_BTN = (By.XPATH, "//button[@type='submit']")