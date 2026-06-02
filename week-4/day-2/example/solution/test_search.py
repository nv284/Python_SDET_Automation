def test_search(browser):

    browser.get("https://www.google.com")

    print(browser.title)

    assert "Google" in browser.title