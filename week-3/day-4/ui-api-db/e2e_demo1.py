import requests
import mysql.connector

# -----------------------
# UI Input
# -----------------------
name = input("Enter Employee Name: ")
job = input("Enter Job: ")

# -----------------------
# API Call
# -----------------------
url = "https://reqres.in/api/users"

payload = {
    "name": name,
    "job": job
}

response = requests.post(url, json=payload)

print("API Status Code:", response.status_code)

# -----------------------
# DB Connection
# -----------------------
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="pass",
    database="company_db"
)

cursor = conn.cursor()

# Insert data into DB
sql = """
INSERT INTO employees(id, name, job)
VALUES (%s, %s, %s)
"""

employee_id = 102

cursor.execute(sql, (employee_id, name, job))

conn.commit()

print("Data inserted into MySQL")

# -----------------------
# Validation
# -----------------------
cursor.execute(
    "SELECT * FROM employees WHERE id = %s",
    (employee_id,)
)

record = cursor.fetchone()

print("DB Record:", record)

cursor.close()
conn.close()