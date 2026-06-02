def test_login(browser):

    browser.get("https://www.google.com")

    assert "Google" in browser.title
