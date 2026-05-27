import sqlite3

# Connect Database
connection = sqlite3.connect("company.db")

# Create Cursor
cursor = connection.cursor()

#----------------------------------------

# -----------------------------------
# STEP 2 → Create users Table
# -----------------------------------

cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY,
    name TEXT,
    email TEXT
)
""")

print("users table created")

# -----------------------------------
# STEP 3 → Create orders Table
# -----------------------------------

cursor.execute("""
CREATE TABLE IF NOT EXISTS orders (
    order_id INTEGER PRIMARY KEY,
    user_id INTEGER,
    product TEXT
)
""")

print("orders table created")

# -----------------------------------
# STEP 4 → Insert Data into users Table
# -----------------------------------

cursor.execute("""
INSERT INTO users (id, name, email)
VALUES (1, 'John', 'john@test.com')
""")

cursor.execute("""
INSERT INTO users (id, name, email)
VALUES (2, 'Alice', 'alice@test.com')
""")

print("Users data inserted")
# -----------------------------------
# STEP 5 → Insert Data into orders Table
# -----------------------------------

cursor.execute("""
INSERT INTO orders (order_id, user_id, product)
VALUES (101, 1, 'Laptop')
""")

cursor.execute("""
INSERT INTO orders (order_id, user_id, product)
VALUES (102, 2, 'Mobile')
""")

print("Orders data inserted")

# -----------------------------------
# STEP 6 → Save Changes
# -----------------------------------

connection.commit()

print("Changes committed")

# -----------------------------------
# STEP 7 → Close Database
# -----------------------------------

connection.close()

print("Database closed")