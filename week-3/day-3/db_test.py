import sqlite3

# Connect database
conn = sqlite3.connect("company.db")

# Create cursor
cursor = conn.cursor()

# Create table
cursor.execute("""
CREATE TABLE IF NOT EXISTS TCS_employees (
    id INTEGER PRIMARY KEY,
    name TEXT,
    salary INTEGER
)
""")

# Insert sample data
cursor.execute("""
INSERT INTO TCS_employees(name, salary)
VALUES('Nishi', 75000)
""")

cursor.execute("""
INSERT INTO TCS_employees(name, salary)
VALUES('Mahesh', 65000)
""")

# Save data
conn.commit()

print("Data inserted successfully")

# -----------------------------
# SELECT Query Testing
# -----------------------------

cursor.execute("SELECT * FROM TCS_employees")

rows = cursor.fetchall()

print("\nAll Employee Records")

for row in rows:
    print(row)

# -----------------------------
# WHERE Query Testing
# -----------------------------

cursor.execute("""
SELECT * FROM TCS_employees
WHERE salary > 70000
""")

result = cursor.fetchall()

print("\nEmployees With Salary > 70000")

for data in result:
    print(data)

# -----------------------------
# Validation Logic
# -----------------------------

expected_name = "Nishi"

cursor.execute("""
SELECT name FROM TCS_employees
WHERE id = 1
""")

actual_result = cursor.fetchone()[0]

# Test Validation
if actual_result == expected_name:
    print("\nTEST CASE PASSED")
else:
    print("\nTEST CASE FAILED")

# Close connection
conn.close()