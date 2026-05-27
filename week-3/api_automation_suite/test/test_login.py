from utils.api_client import APIClient
from utils.config import LOGIN_ENDPOINT

client = APIClient()

def test_login_success():

    payload = {
        "username": "emilys",
        "password": "emilyspass"
    }

    response = client.post(
        LOGIN_ENDPOINT,
        payload
    )

    print(response.status_code)
    print(response.text)

    data = response.json()

    assert response.status_code == 200

    assert "accessToken" in data