import requests

url = "https://jsonplaceholder.typicode.com/users/1"

response = requests.get(url)

data = response.json()

# Nested JSON Parsing
print("User Name:", data["name"])
print("Email:", data["email"])
print("City:", data["address"]["city"])
print("Company:", data["company"]["name"])

# Validations
assert response.status_code == 200
assert "@" in data["email"]
assert isinstance(data["address"], dict)

print("\nAdvanced JSON Parsing Passed")