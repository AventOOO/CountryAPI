import requests

API_KEY = "rc_live_04493428440b4c949250cc5d380b4ee6"

BASE_URL = "https://api.restcountries.com/countries/v5/names.common"


def get_country(name: str):

    headers = {
        "Authorization": f"Bearer {API_KEY}"
    }

    url = f"{BASE_URL}/{name}"

    response = requests.get(url, headers=headers)

    if response.status_code != 200:
        return None

    return response.json()