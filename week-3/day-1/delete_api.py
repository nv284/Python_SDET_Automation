import requests

# API URL
url = "https://dummyjson.com/products/1"

# Send DELETE request
response = requests.delete(url)

# Convert response into JSON
data = response.json()

# Print response details
print("Status Code:", response.status_code)

print("\nDeleted Product Details")
print("------------------------")
print("ID:", data["id"])
print("Title:", data["title"])
print("Deleted:", data["isDeleted"])

# Validations
assert response.status_code == 200
assert data["id"] == 1
assert data["isDeleted"] == True

print("\nDELETE API Test Passed")