import mysql.connector

# Database connection
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="pass" ,
    database="company_db"
)

# Create cursor
cursor = conn.cursor()

print("Database Connected Successfully")

# Insert data
query = "INSERT INTO users (id, name, job) VALUES (%s, %s, %s)"

values = (102, "Riya", "QA")

cursor.execute(query, values)

# Save changes
conn.commit()

print("Data Inserted Successfully")

# Fetch data
cursor.execute("SELECT * FROM users")

result = cursor.fetchall()

print("\nUser Records:")

for row in result:
    print(row)

# Close connection
cursor.close()
conn.close()