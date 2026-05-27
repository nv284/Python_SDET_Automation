from utils.api_client import APIClient
from utils.config import USERS_ENDPOINT

client = APIClient()

def test_get_users():

    response = client.get(USERS_ENDPOINT)

    data = response.json()

    assert response.status_code == 200

    assert "users" in data