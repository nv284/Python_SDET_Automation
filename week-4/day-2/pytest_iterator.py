import pytest

@pytest.fixture
def status_cycler():
    """Cycles through different order statuses sequentially."""
    statuses = ["pending", "processing", "shipped", "delivered"]
    iterator = iter(statuses)
    return lambda: next(iterator)

def test_order_progression(status_cycler):
    # Each call mimics a state transition pattern
    assert status_cycler() == "pending"
    assert status_cycler() == "processing"
    assert status_cycler() == "shipped"
