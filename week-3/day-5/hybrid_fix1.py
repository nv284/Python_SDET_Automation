import random
import re
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By


def test_real_hybrid_login():
    # Generate a completely unique username every run to prevent "User already exists" conflicts
    unique_id = random.randint(10000, 99999)
    username = f"hybrid_user_{unique_id}"
    password = "SecurePassword123!"

    print(f"--- STARTING SCENARIO FOR USER: {username} ---")

    # --- STEP 1: Dynamic API Registration (Pre-requisite Injection) ---
    signup_url = "https://api.demoblaze.com/signup"
    signup_payload = {"username": username, "password": password}

    signup_response = requests.post(signup_url, json=signup_payload)
    assert (
        signup_response.status_code == 200
    ), "Database Injection Phase: API Registration failed"
    print("1. API Signup Phase Passed. User created directly in backend database.")

    # --- STEP 2: Instant Backend API Authentication ---
    login_url = "https://api.demoblaze.com/login"
    login_payload = {"username": username, "password": password}

    login_response = requests.post(login_url, json=login_payload)
    assert (
        login_response.status_code == 200
    ), f"API Error! HTTP status code is: {login_response.status_code}"

    # Safely extract the token string using regex
    raw_text = login_response.text
    token_match = re.search(r"Auth_token:\s*([^\s\"]+)", raw_text)

    if not token_match:
        raise ValueError(
            f"Failed to find expected token in API response: {raw_text}"
        )

    token = token_match.group(1)
    print(f"2. API Authentication Passed. Token generated: {token[:15]}...")

    # --- STEP 3: Browser Context Handshake ---
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)

    try:
        # Load the target domain first so the browser allows us to write to storage
        driver.get("https://www.demoblaze.com/")

        # --- STEP 4: Injecting the Hybrid Payload via JavaScript ---
        # Inject the newly registered user's credentials into HTML5 sessionStorage
        driver.execute_script(f"sessionStorage.setItem('tokenp_', '{token}');")
        driver.execute_script(f"sessionStorage.setItem('user', '{username}');")
        print("3. Hybrid Sync Phase Passed. Session parameters written.")

        # --- STEP 5: Frontend Refresh & Verification ---
        driver.refresh()

        # Locate the welcoming navigation element that displays user context profile identity
        welcome_element = driver.find_element(By.ID, "nameofuser")

        assert (
            username in welcome_element.text
        ), f"UI Error! Element displayed unexpected text: '{welcome_element.text}'"
        print(
            f"4. UI Phase Passed. Dashboard active. Welcome banner says: '{welcome_element.text}'"
        )

    finally:
        # Close browser instance safely
        driver.quit()


if __name__ == "__main__":
    test_real_hybrid_login()
