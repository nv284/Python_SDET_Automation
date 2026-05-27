import requests

# -----------------------------------
# STEP 1 → Login Payload
# -----------------------------------

login_payload = {
    "username": "emilys",
    "password": "emilyspass"
}

# -----------------------------------
# STEP 2 → Token Generation API Call
# -----------------------------------

login_response = requests.post(
    "https://dummyjson.com/auth/login",
    json=login_payload
)

# -----------------------------------
# STEP 3 → Validate Login Response
# -----------------------------------

print("Login Status Code:", login_response.status_code)

assert login_response.status_code == 200

# -----------------------------------
# STEP 4 → Convert Response to JSON
# -----------------------------------

login_data = login_response.json()

print("Login Response:", login_data)

# -----------------------------------
# STEP 5 → Extract Access Token
# -----------------------------------

token = login_data["accessToken"]

print("Generated Token:", token)

# -----------------------------------
# STEP 6 → Prepare Authorization Header
# -----------------------------------

headers = {
    "Authorization": f"Bearer {token}"
}

# -----------------------------------
# STEP 7 → Consume Token in Secured API
# -----------------------------------

user_response = requests.get(
    "https://dummyjson.com/auth/me",
    headers=headers
)

# -----------------------------------
# STEP 8 → Validate Secured API Response
# -----------------------------------

print("User API Status Code:", user_response.status_code)

assert user_response.status_code == 200

# -----------------------------------
# STEP 9 → Parse User Response
# -----------------------------------

user_data = user_response.json()

print("User Response:", user_data)

# -----------------------------------
# STEP 10 → Response Validation
# -----------------------------------

assert "email" in user_data

print("User Email:", user_data["email"])