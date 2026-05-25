#A production issue was reported where:
#Product/User details were displaying incorrectly in UI
#Some API responses had missing fields ,Response schema was inconsistent,Null values caused frontend crashes
#Incorrect status codes were returned
#As an API Automation Tester, your responsibility is to validate:
#Response status code ,Response body , Mandatory fields ,Data types ,Null values
import requests

import requests

# API URL
url = "https://jsonplaceholder.typicode.com/users/1"

# Send GET request
response = requests.get(url)

# Convert response into JSON
data = response.json()

# Print response
print("Response Data")
print("----------------")
print(data)

# -----------------------------
# Response Validations
# -----------------------------

# Validate Status Code
assert response.status_code == 200
print("Status Code Validation Passed")

# Validate User ID
assert data["id"] == 1
print("User ID Validation Passed")

# Validate Email
assert "@" in data["email"]
print("Email Validation Passed")

# Validate Name is not null
assert data["name"] is not None
print("Null Validation Passed")

# Validate Nested JSON
assert "city" in data["address"]
print("Nested JSON Validation Passed")

# Validate Company Name
assert "name" in data["company"]
print("Company Validation Passed")

# Validate Response Time
assert response.elapsed.total_seconds() < 2
print("Response Time Validation Passed")

print("\nAll API Response Validations Passed Successfully")