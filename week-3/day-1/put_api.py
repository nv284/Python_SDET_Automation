import requests

# API URL
url = "https://dummyjson.com/products/1"

# Updated Payload
payload = {
    "title": "Updated iPhone 15 Pro",
    "price": 1999
}

# Send PUT Request
response = requests.put(url, json=payload)

# Convert response to JSON
data = response.json()

# Print response details
print("Status Code:", response.status_code)

print("\nUpdated Product Details")
print("-------------------------")
print("ID:", data["id"])
print("Title:", data["title"])
print("Price:", data["price"])

# Validations
assert response.status_code == 200
assert data["title"] == "Updated iPhone 15 Pro"
assert data["price"] == 1999

print("\nPUT API Test Passed")