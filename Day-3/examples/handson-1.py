#Create Reusable Utility Functions for Automation Testing

#A QA automation engineer wants to build small reusable utility functions for a testing framework.

#The automation utility should:

#Validate usernames
#Validate passwords
#Print test execution status
#Generate execution summary
#Reuse the same functions multiple times

# =========================================
# MINI AUTOMATION UTILITIES
# =========================================


# Utility Function 1
# Validate Username

def validate_username(username):

    if len(username) >= 5:
        return True

    else:
        return False


# Utility Function 2
# Validate Password

def validate_password(password):

    if len(password) >= 6:
        return True

    else:
        return False


# Utility Function 3
# Print Test Status

def print_test_status(test_name, result):

    print("\nTest Case :", test_name)
    print("Result    :", result)


# Utility Function 4
# Execution Summary

def execution_summary(total, passed, failed):

    print("\n========== EXECUTION SUMMARY ==========")
    print("Total Test Cases :", total)
    print("Passed           :", passed)
    print("Failed           :", failed)


# =========================================
# BULK TEST DATA
# =========================================

users = [
    ["admin", "admin123"],
    ["qa", "qa12"],
    ["automation_user", "auto12345"],
    ["ab", "123"],
    ["tester01", "test@123"]
]


# =========================================
# AUTOMATION EXECUTION
# =========================================

total_test_cases = 0
passed_test_cases = 0
failed_test_cases = 0


print("===== AUTOMATION EXECUTION STARTED =====")


for user in users:

    username = user[0]
    password = user[1]

    total_test_cases = total_test_cases + 1

    username_result = validate_username(username)
    password_result = validate_password(password)

    # Validation Logic

    if username_result == True and password_result == True:

        print_test_status(username, "PASS")
        passed_test_cases = passed_test_cases + 1

    else:

        print_test_status(username, "FAIL")
        failed_test_cases = failed_test_cases + 1


# =========================================
# FINAL SUMMARY
# =========================================

execution_summary(
    total_test_cases,
    passed_test_cases,
    failed_test_cases
)