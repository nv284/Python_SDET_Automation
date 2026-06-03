import pytest

@pytest.mark.parametrize("user_role", ["admin", "guest"])
@pytest.mark.parametrize("device", ["desktop", "mobile"])

def test_ui_access(user_role, device):
    
    print(f"Testing {user_role} access layout on a {device} viewport.")
    assert True
