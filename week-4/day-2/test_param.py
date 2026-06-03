import pytest


def is_valid_email(email):
    return "@" in email and email.endswith(".com")


# 1. Attach the parametrize decorator to feed data
@pytest.mark.parametrize(
    "test_input, expected_result",
    [
        ("user@example.com", True),      
        ("hello@domain.com", True),       
        ("plainaddress", False),          
        ("user@domain.org", False),       
        ("@missingusername.com", True)   
    ]
)

def test_email_validation(test_input, expected_result):
   
    assert is_valid_email(test_input) == expected_result