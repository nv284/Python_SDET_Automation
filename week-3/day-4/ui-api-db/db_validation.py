import mysql.connector

# Connect to MySQL

connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="pass",      # Change as per your system
    database="company_db"
)

cursor = connection.cursor()

# Execute Query

query = "SELECT name FROM employees WHERE id = 101"

cursor.execute(query)

result = cursor.fetchone()

# Expected Value

expected_name = "John"

# Validation

if result[0] == expected_name:
    print("PASS - Backend data is correct")
else:
    print("FAIL - Backend data is incorrect")

# Close connection

cursor.close()
connection.close()