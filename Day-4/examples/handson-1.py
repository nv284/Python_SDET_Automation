#A QA automation engineer wants to build a reusable automation framework using Python classes.

#The automation module should:

#Store test case information
#Execute test cases
#Display execution status
#Generate final execution report

#The goal is to organize automation logic using:

#Classes
#Objects
#Methods
#Constructors

#This simulates how real-world automation frameworks are designed in:

#Selenium ,PyTest , Robot Framework ,Automotive validation frameworks

# =========================================
# CLASS-BASED AUTOMATION MODULE
# =========================================


# Create Class

class AutomationFramework:


    # Constructor
    # Automatically executes when object is created

    def __init__(self):

        self.total_test_cases = 0
        self.passed_test_cases = 0
        self.failed_test_cases = 0


    # Method 1
    # Execute Test Case

    def execute_test(self, test_name, status):

        print("\nExecuting Test :", test_name)

        self.total_test_cases = self.total_test_cases + 1


        # Validation Logic

        if status == "PASS":

            print("Execution Status : PASS")

            self.passed_test_cases = self.passed_test_cases + 1


        elif status == "FAIL":

            print("Execution Status : FAIL")

            self.failed_test_cases = self.failed_test_cases + 1


        else:

            print("Execution Status : SKIPPED")


    # Method 2
    # Display Final Report

    def display_report(self):

        print("\n========== FINAL EXECUTION REPORT ==========")

        print("Total Test Cases :", self.total_test_cases)
        print("Passed Tests     :", self.passed_test_cases)
        print("Failed Tests     :", self.failed_test_cases)



# =========================================
# CREATE OBJECT
# =========================================

framework = AutomationFramework()


# =========================================
# EXECUTE TEST CASES
# =========================================

framework.execute_test("Login Test", "PASS")

framework.execute_test("Payment Test", "PASS")

framework.execute_test("Camera Validation", "FAIL")

framework.execute_test("Bluetooth Testing", "PASS")

framework.execute_test("GPU Stress Test", "FAIL")

framework.execute_test("Voice Assistant Test", "SKIPPED")


# =========================================
# DISPLAY FINAL REPORT
# =========================================

framework.display_report()