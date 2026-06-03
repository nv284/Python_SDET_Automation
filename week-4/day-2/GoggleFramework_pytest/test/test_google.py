from config.config import SEARCH_TEXT
from pages.google_page import GooglePage

def test_google_search(browser):

    page = GooglePage(browser)

    page.search(SEARCH_TEXT)

    assert "Google" in browser.title
