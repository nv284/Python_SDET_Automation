from driver_setup import driver
from login_page import LoginPage
from test_data import username, password

driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

driver.implicitly_wait(10)

driver.find_element(
    *LoginPage.USERNAME
).send_keys(username)

driver.find_element(
    *LoginPage.PASSWORD
).send_keys(password)

driver.find_element(
    *LoginPage.LOGIN_BTN
).click()

print("Login Successful")

input("Press Enter to close browser...")

driver.quit()
