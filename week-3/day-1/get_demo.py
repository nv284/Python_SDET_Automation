# your application needs to display a profile page for User id 2.
# write an automated test script to fetch this user's details 
# and verify the server successfully finds them (status code 200)

import json

import requests
# 1.  define base url 
url = "https://reqres.in/api/users/2"

# 2. Send the HTTP GET request
response = requests.get(url)

# 3. Print the raw status code and the JSON data for visibility
print(f"Status Code: {response.status_code}")
print("Response Body JSON:")
print(response.json())


# 4 automate the varification  (Asserting the outcome)
assert response.status_code == 200 , f"Expected 200 , but got {response.status_code }"

#Extract data to confirm we got the right user
json_data = response.json()
assert json_data["data"] ["id"] == 2 , "The user ID does not match !"

print("Test Passed : User fetched successfully !")