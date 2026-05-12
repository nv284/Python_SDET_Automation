##Process Bulk Test Data
#Problem Statement

#A QA automation engineer has multiple users for login testing.

#Process all users using loops:

#Check username length
#Validate password length
#Print VALID or INVALID user

# Bulk test data

users = [
    ["admin", "admin123"],
    ["qa", "qa123"],
    ["automation_user", "auto12345"],
    ["ab", "123"],
    ["tester01", "test@123"]
]

print("===== BULK USER VALIDATION =====")

for user in users:

    username = user[0]
    password = user[1]

    print("\nChecking User:", username)

    if len(username) >= 5:

        if len(password) >= 6:
            print("VALID USER")

        else:
            print("INVALID PASSWORD")

    else:
        print("INVALID USERNAME")