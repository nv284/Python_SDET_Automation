import requests
from utils.config import BASE_URL

class APIClient:

    def get(self, endpoint, headers=None):

        return requests.get(
            BASE_URL + endpoint,
            headers=headers
        )

    def post(self, endpoint, payload, headers=None):

        return requests.post(
            BASE_URL + endpoint,
            json=payload,
            headers=headers
        )