import pytest
from pages.login_page import LoginPage

@pytest.mark.smoke  #  Smoke tag
def test_successful_login(driver, config):
    login_page = LoginPage(driver, timeout=config["timeout"])
    
    login_page.navigate_to(config["base_url"])
    # "standard_user" and "secret_sauce" are default valid credentials here
    login_page.login_with_credentials("standard_user", "secret_sauce")
    
    # Assert successful landing page url redirection
    assert "inventory.html" in driver.current_url

@pytest.mark.regression  #  Regression tag
def test_invalid_login(driver, config):
    login_page = LoginPage(driver, timeout=config["timeout"])
    
    login_page.navigate_to(config["base_url"])
    login_page.login_with_credentials("locked_out_user", "wrong_password")
    
    # Assert error block content
    error_text = login_page.get_error_message()
    assert "Username and password do not match any user in this service" in error_text
