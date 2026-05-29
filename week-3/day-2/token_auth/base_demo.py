import requests
import json

# 1. Setup the website URL
BASE_URL = "https://reqres.in"

# 2. Login to get the token
login_data = {
    "email": "eve.holt@reqres.in",  # ReqRes default test user
    "password": "cityslickica"
}

login_response = requests.post(f"{BASE_URL}/login", json=login_data)
token = login_response.json()["token"]
print(f" Step 1 Success! Grabbed Token: {token}")

# 3. Use the token to access a secured page
headers = {
    "Authorization": f"Bearer {token}"
}

# Fetching user data using our token header
user_response = requests.get(f"{BASE_URL}/users/2", headers=headers)

# 4. Check if it worked (QA Assertion)
assert user_response.status_code == 200
print(" Step 2 Success! API allowed us in using the token.")
print(user_response.json())
