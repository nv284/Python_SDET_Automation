import requests

# API URL
url = "https://jsonplaceholder.typicode.com/posts/1"

# Send GET request
response = requests.get(url)

# Convert JSON response into Python dictionary
data = response.json()

# Print complete JSON response
print("Complete JSON Response")
print("------------------------")
print(data)

# JSON Parsing
print("\nParsed Values")
print("------------------------")
print("User ID:", data["userId"])
print("Post ID:", data["id"])
print("Title:", data["title"])
print("Body:", data["body"])

# Validations
assert response.status_code == 200
assert data["id"] == 1
assert isinstance(data["title"], str)

print("\nJSON Parsing Validation Passed")