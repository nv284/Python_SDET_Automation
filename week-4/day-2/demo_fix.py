import pytest

# Define the fixture to handle the setup
@pytest.fixture
def cart():
    """Provides a fresh, empty list for each test."""
    return []

# The fixture is passed as an argument to the test functions
def test_add_item(cart):
    cart.append("apple")
    assert len(cart) == 1

def test_cart_empty(cart):
    assert len(cart) == 0
