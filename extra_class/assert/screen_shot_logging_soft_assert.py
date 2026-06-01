class SoftAssert:

    def __init__(self):
        self.failures = []

    def assert_equal(self, actual, expected, message=""):
        if actual != expected:
            self.failures.append(
                f"[FAILED] {message} "
                f"Expected={expected} "
                f"Actual={actual}"
            )

    def assert_all(self):
        if self.failures:

            print("\n========== TEST FAILURES ==========\n")

            for failure in self.failures:
                print(failure)

            raise AssertionError(
                f"\nTotal Failures: {len(self.failures)}"
            )

        print("\nAll Assertions Passed")