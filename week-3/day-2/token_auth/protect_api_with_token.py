#After login, use token in protected API.

import requests

# Protected API
url = "https://dummyjson.com/auth/me"

# Token received from login API
token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6MSwidXNlcm5hbWUiOiJlbWlseXMiLCJlbWFpbCI6ImVtaWx5LmpvaG5zb25AeC5kdW1teWpzb24uY29tIiwiZmlyc3ROYW1lIjoiRW1pbHkiLCJsYXN0TmFtZSI6IkpvaG5zb24iLCJnZW5kZXIiOiJmZW1hbGUiLCJpbWFnZSI6Imh0dHBzOi8vZHVtbXlqc29uLmNvbS9pY29uL2VtaWx5cy8xMjgiLCJpYXQiOjE3Nzk3Mzc0MTMsImV4cCI6MTc3OTc0MTAxM30.I2o68TxbxZDLq0gLChPXvH-lFERjM9xh-xEn8r46DXs"

# Authorization Header
headers = {
    "Authorization": f"Bearer {token}"
}

# Send GET request
response = requests.get(url, headers=headers)

# Print response
print(response.status_code)
print(response.json())