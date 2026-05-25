import requests

# API URL
url = "https://dummyjson.com/products/add"

# Request Payload
payload = {
    "title": "iPhone 15 Pro",
    "price": 1499,
    "category": "smartphones"
}

# Send POST request
response = requests.post(url, json=payload)

# Print Status Code
print("Status Code:", response.status_code)

# Print JSON Response
data = response.json()

print("\nProduct Created Successfully")
print("----------------------------")
print("Product ID:", data["id"])
print("Title:", data["title"])
print("Price:", data["price"])
print("Category:", data["category"])

# Validation
if response.status_code == 201:
    print("\nPOST API Test Passed")
else:
    print("\nPOST API Test Failed")