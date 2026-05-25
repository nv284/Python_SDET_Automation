#In Token-Based Authentication:

#---User logs in with username/password
#---Server generates a token
#---Client sends token in every API request
#---Server validates token
#---Access is granted

import requests

# Login API URL
url = "https://dummyjson.com/auth/login"

# Login Payload
payload = {
    "username": "emilys",
    "password": "emilyspass"
}

# Send POST request
response = requests.post(url, json=payload)

# Convert response into JSON
data = response.json()

# Print response
print("Status Code:", response.status_code)

# Extract token
token = data["accessToken"]

print("\nGenerated Token")
print("----------------")
print(token)

# Validation
assert response.status_code == 200
assert token is not None

print("\nAuthentication Successful")

