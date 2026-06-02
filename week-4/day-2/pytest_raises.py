import pytest

# 1. The Application Code
def withdraw_money(balance, amount):
    """Withdraws money from an account. Raises ValueError for invalid actions."""
    if amount <= 0:
        raise ValueError("Withdrawal amount must be positive.")
    if amount > balance:
        raise ValueError("Insufficient funds available.")
    return balance - amount


# 2. The Pytest Unit Tests

def test_negative_withdrawal_raises_error():
    """Test 1: Standard usage checking for the correct exception type."""
    with pytest.raises(ValueError):
        withdraw_money(balance=100, amount=-50)


def test_insufficient_funds_matches_message():
    """Test 2: Using the 'match' parameter to verify the specific error message."""
    with pytest.raises(ValueError, match="Insufficient funds available."):
        withdraw_money(balance=20, amount=50)


def test_exception_object_details():
    """Test 3: Capturing exception info to inspect properties after execution."""
    with pytest.raises(ValueError) as exc_info:
        withdraw_money(balance=100, amount=0)
        
    # Verify exact details using the captured exc_info object
    assert exc_info.type is ValueError
    assert "must be positive" in str(exc_info.value)
