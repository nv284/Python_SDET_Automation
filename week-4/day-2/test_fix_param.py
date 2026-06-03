import pytest

@pytest.fixture
def mock_db():
    return {"status": "connected", "records": []}

@pytest.mark.parametrize("username", ["alice", "bob", "charlie"])
def test_user_creation(mock_db, username):
    # The static fixture (mock_db) and dynamic arguments work together
    mock_db["records"].append(username)
    assert username in mock_db["records"]
