import requests

def test_get_users():

    url = "https://reqres.in/api/users?page=2"

    headers = {
        "x-api-key": "reqres-free-v1"
    }

    response = requests.get(url, headers=headers)

    assert response.status_code == 200