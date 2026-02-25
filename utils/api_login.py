import requests


def get_auth_token(email, password):
    url = "https://rahulshettyacademy.com/api/ecom/auth/login"

    payload = {
        "userEmail": email,
        "userPassword": password
    }

    response = requests.post(url, json=payload)
    response.raise_for_status()

    return response.json()["token"]