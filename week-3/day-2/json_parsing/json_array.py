import requests

url = "https://jsonplaceholder.typicode.com/posts"

response = requests.get(url)

# Convert JSON array into Python list
data = response.json()

print("Total Posts:", len(data))

# Access first record
first_post = data[0]

print("\nFirst Post Details")
print("--------------------")
print("ID:", first_post["id"])
print("Title:", first_post["title"])

# Validations
assert response.status_code == 200
assert len(data) > 0
assert "title" in first_post

print("\nJSON Array Parsing Passed")