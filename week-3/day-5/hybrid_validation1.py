import re
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By


def test_real_hybrid_login():
    # --- STEP 1: Backend API Authentication ---
    login_api_url = "https://api.demoblaze.com/login"
    payload = {
        "username": "test_hybrid_user",
        "password": "Password123!",  # Clean registered test user credentials
    }

    response = requests.post(login_api_url, json=payload)

    # Validate that the backend API successfully responded
    assert (
        response.status_code == 200
    ), f"API Error! HTTP status code is: {response.status_code}"

    # Safely extract the token string using regex to avoid IndexError
    # The endpoint returns a response raw body text string: "Auth_token: <token_value>"
    raw_text = response.text
    token_match = re.search(r"Auth_token:\s*([^\s\"]+)", raw_text)

    if not token_match:
        raise ValueError(
            f"Failed to find expected token in API response: {raw_text}"
        )

    token = token_match.group(1)
    print(f"1. API Phase Passed. Token clean extraction: {token[:15]}...")

    # --- STEP 2: Browser Context Handshake ---
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)

    try:
        # Load the target domain first so the browser allows us to write to storage
        driver.get("https://www.demoblaze.com/")

        # --- STEP 3: Injecting the Hybrid Payload via JavaScript ---
        # We manually update HTML5 sessionStorage properties via JavaScript
        driver.execute_script(f"sessionStorage.setItem('tokenp_', '{token}');")
        driver.execute_script(
            "sessionStorage.setItem('user', 'test_hybrid_user');"
        )
        print("2. Hybrid Sync Phase Passed. Session parameters written.")

        # --- STEP 4: Frontend Refresh & Verification ---
        driver.refresh()

        # Locate the specific welcoming nav element that displays your profile identity
        welcome_element = driver.find_element(By.ID, "nameofuser")

        assert (
            "test_hybrid_user" in welcome_element.text
        ), f"UI Error! Element displayed unexpected text: '{welcome_element.text}'"
        print(f"3. UI Phase Passed. Dashboard active: {welcome_element.text}")

    finally:
        # Close browser instance safely
        driver.quit()


if __name__ == "__main__":
    test_real_hybrid_login()
