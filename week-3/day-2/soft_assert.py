import pytest_check as check

response = {
    "name": "John",
    "job": "Developer",
    "city": "Mumbai"
}

check.equal(response["name"], "John")

check.equal(response["job"], "Tester")

check.equal(response["city"], "Pune")

check.equal(10, 20, "Number mismatch")

check.equal("John", "Mike", "Name mismatch")

print("Execution Continues")