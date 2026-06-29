import requests
from fastapi import HTTPException

API_KEY = "rc_live_04493428440b4c949250cc5d380b4ee6"
BASE_URL = "https://api.restcountries.com/countries/v5/names.common"


def get_country(name: str):
    headers = {
        "Authorization": f"Bearer {API_KEY}"
    }

    url = f"{BASE_URL}/{name}"
    response = requests.get(url, headers=headers)

    # Проверяем ответ API
    if response.status_code != 200:
        raise HTTPException(
            status_code=response.status_code,
            detail="Ошибка при обращении к REST Countries API"
        )

    data = response.json()

    # Получаем список стран
    objects = data.get("data", {}).get("objects", [])

    # Если список пустой
    if not objects:
        raise HTTPException(
            status_code=404,
            detail=f'Страна "{name}" не найдена'
        )

    country = objects[0]

    return {
        "country": country["names"]["common"],
        "official_name": country["names"]["official"],
        "capital": country["capitals"][0]["name"],
        "population": country["population"],
        "area": country["area"]["kilometers"],
        "region": country["region"],
        "subregion": country["subregion"],
        "language": country["languages"][0]["name"],
        "currency": country["currencies"][0]["name"],
        "flag": country["flag"]["emoji"]
    }
