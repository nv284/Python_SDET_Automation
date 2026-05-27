import json
import pytest

from utils.api_client import APIClient
from utils.config import LOGIN_ENDPOINT

client = APIClient()

with open("data/login_data.json") as file:
    test_data = json.load(file)

@pytest.mark.parametrize("payload", test_data)

def test_multiple_login(payload):

    response = client.post(
        LOGIN_ENDPOINT,
        payload
    )

    print(response.status_code)

    assert response.status_code in [200, 400]