import sys
import pytest
# 1. Always skipped
@pytest.mark.skip(reason="This feature is deprecated and no longer works")
def test_old_code():
    assert True
# 2. Skipped ONLY if running on a Python version older than 3.8
@pytest.mark.skipif(sys.version_info < (3,8), reason="Requires Python 3.8 or higher")
def test_modern_syntax():
    # Example syntax that breaks on very old Python versions
    walrus_operator_test = (x := 10)
    assert walrus_operator_test == 10

# 3. Runs but will not break your build if it fails
@pytest.mark.xfail(reason="Bug #904: External API payment gateway is down")
def test_payment_gateway():
    # This assertion fails, but pytest records it as XFAIL (Expected Failure)
    assert False 
