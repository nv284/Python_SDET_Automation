#Null Validation Methods ---> 
# Method 1 — Using is None ---if data["description"] is 
# None: print("NULL Value")
#  and Method 2 — Using Assertion ----
#  assert data["description"] is None
import requests

url = "https://jsonplaceholder.typicode.com/users/1"

response = requests.get(url)

data = response.json()

# Add sample null field
data["secondaryEmail"] = None

# Validation
assert data["secondaryEmail"] is None

print("Secondary Email is NULL")
print("Validation Passed")