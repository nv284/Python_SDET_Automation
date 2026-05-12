#Loop-Driven Automation Scenario
#Problem Statement -An automation framework executes regression tests for multiple modules.
#Rules:

#Execute all test cases
#Skip disabled test cases
#Stop execution if CRITICAL failure happens

# Automation test execution

test_cases = [
    ["Login Test", "ENABLED"],
    ["Payment Test", "ENABLED"],
    ["Camera Validation", "DISABLED"],
    ["GPU Stress Test", "ENABLED"],
    ["Critical ECU Test", "FAILED"],
    ["Bluetooth Test", "ENABLED"]
]

print("===== AUTOMATION EXECUTION STARTED =====")

for test in test_cases:

    test_name = test[0]
    status = test[1]

    # Skip disabled tests
    if status == "DISABLED":
        print("\nSkipping:", test_name)
        continue

    # Stop execution on critical failure
    if status == "FAILED":
        print("\nCRITICAL FAILURE FOUND")
        print("Stopping Execution:", test_name)
        break

    print("\nExecuting:", test_name)
    print("Execution Successful")

print("\n===== EXECUTION FINISHED =====")