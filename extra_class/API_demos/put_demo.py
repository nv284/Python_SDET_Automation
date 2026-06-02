import requests
import mysql.connector
from selenium import webdriver
import time

# -----------------------------
# Connect to MySQL
# -----------------------------
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="pass",  # Replace with your actual password
    database="company_db"
)

cursor = db.cursor()

# -----------------------------
# Fetch User Data from DB
# -----------------------------
cursor.execute("""
SELECT id, name
FROM users
WHERE id = 11
""")

row = cursor.fetchone()

# Check if record exists
if row is None:
    print("No user found with id = 11")
    cursor.close()
    db.close()
    exit()

user_id = row[0]
new_name = row[1]

print("User ID:", user_id)
print("Name:", new_name)

# -----------------------------
# PUT API Request
# -----------------------------
url = f"https://reqres.in/api/users/{user_id}"

payload = {
    "name": new_name,
    "job": "Engineer"
}

response = requests.put(
    url,
    json=payload
)

print("\nStatus Code:", response.status_code)
print("Response:", response.json())

# -----------------------------
# Validate API Response
# -----------------------------
if response.status_code == 200:

    response_json = response.json()

    assert response_json["name"] == new_name
    assert response_json["job"] == "Engineer"

    print("User updated successfully.")

    # -----------------------------
    # Update DB Audit Column
    # -----------------------------
    cursor.execute("""
    UPDATE users
    SET last_updated = NOW()
    WHERE id = %s
    """, (user_id,))

    db.commit()

    print("Database updated successfully.")

else:
    print("Failed to update user.")

# -----------------------------
# Selenium Verification
# -----------------------------
driver = webdriver.Chrome()

driver.maximize_window()

driver.get("https://reqres.in")

print("\nWebsite Title:", driver.title)

assert "Reqres" in driver.title, \
    "Title does not contain 'Reqres'"

print("Website verification passed.")

time.sleep(3)

driver.quit()

# -----------------------------
# Close DB Connection
# -----------------------------
cursor.close()
db.close()

print("\nExecution Completed Successfully")