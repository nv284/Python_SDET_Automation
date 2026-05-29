import requests
import mysql.connector
from datetime import datetime

# ==========================================
# STEP 1 - SIMULATED UI INPUT
# ==========================================

print("========== UI INPUT ==========")

user_name = "John Doe"
user_job = "QA Engineer"

print("Entered Name :", user_name)
print("Entered Job  :", user_job)

# ==========================================
# STEP 2 - API REQUEST
# ==========================================

print("\n========== API REQUEST ==========")

url = "https://jsonplaceholder.typicode.com/users"

payload = {
    "name": user_name,
    "job": user_job
}

headers = {
    "Content-Type": "application/json"
}

response = requests.post(
    url=url,
    json=payload,
    headers=headers
)

print("Status Code :", response.status_code)

# ==========================================
# STEP 3 - API VALIDATION
# ==========================================

if response.status_code == 201:
    print("API Call Successful")
else:
    print("API Call Failed")
    print(response.text)
    exit()

# ==========================================
# STEP 4 - JSON RESPONSE PARSING
# ==========================================

response_data = response.json()

print("\nAPI Response:")
print(response_data)

api_id = response_data.get("id", 110)

# Create timestamp manually
created_at = datetime.now()

print("Generated User ID :", api_id)
print("Created At        :", created_at)

# ==========================================
# STEP 5 - MYSQL DATABASE CONNECTION
# ==========================================

print("\n========== DATABASE CONNECTION ==========")

connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="pass",     # Change to your MySQL password
    database="company_db"
)

cursor = connection.cursor()

print("Connected to MySQL Successfully")

# ==========================================
# STEP 6 - INSERT DATA INTO DATABASE
# ==========================================

print("\n========== INSERT DATA ==========")

insert_query = """
INSERT INTO users (id, name, job, createdAt)
VALUES (%s, %s, %s, %s)
"""

values = (
    api_id,
    user_name,
    user_job,
    created_at
)

cursor.execute(insert_query, values)

connection.commit()

print("Data Inserted Successfully")

# ==========================================
# STEP 7 - DATABASE VALIDATION
# ==========================================

print("\n========== DATABASE VALIDATION ==========")

select_query = """
SELECT * FROM users
WHERE id = %s
"""

cursor.execute(select_query, (api_id,))

result = cursor.fetchone()

print("Database Record:")
print(result)

# ==========================================
# STEP 8 - END-TO-END VALIDATION
# ==========================================

print("\n========== END-TO-END VALIDATION ==========")

if result[1] == user_name and result[2] == user_job:
    print("END-TO-END VALIDATION PASSED")
else:
    print("VALIDATION FAILED")

# ==========================================
# STEP 9 - CLOSE CONNECTION
# ==========================================

cursor.close()
connection.close()

print("\nDatabase Connection Closed")