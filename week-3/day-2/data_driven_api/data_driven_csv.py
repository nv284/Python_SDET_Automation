import requests
import csv

# API URL
url = "https://jsonplaceholder.typicode.com/users"

# Open CSV file
with open("week-3\\day-2\\data_driven_api\\user.csv", newline='') as csvfile:

    reader = csv.DictReader(csvfile)

    # Loop through CSV rows
    for row in reader:

        print("\nExecuting API for:", row["name"])

        # Payload from CSV
        payload = {
            "name": row["name"],
            "username": row["username"],
            "email": row["email"]
        }

        # Send POST request
        response = requests.post(url, json=payload)

        # Convert response into JSON
        data = response.json()

        # Print response
        print("Status Code:", response.status_code)
        print("Response:", data)

        # Validations
        assert response.status_code == 201
        assert data["name"] == row["name"]
        assert data["email"] == row["email"]

        print("Validation Passed")