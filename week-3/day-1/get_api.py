import requests

# API URL
url = "https://dummyjson.com/products"

# Send GET request
response = requests.get(url)

# Print Status Code
print("Status Code:", response.status_code)

# Convert response into JSON
data = response.json()

# Print total products
print("Total Products:", data["total"])

# Print first product details
first_product = data["products"][2]

print("\nFirst Product Details")
print("----------------------")
print("Title:", first_product["title"])
print("Price:", first_product["price"])
print("Category:", first_product["category"])

# Validation
if response.status_code == 200:
    print("\nAPI Test Passed")
else:
    print("\nAPI Test Failed")