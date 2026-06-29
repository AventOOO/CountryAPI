import requests
from fastapi import HTTPException
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("API_KEY")

BASE_URL = "https://api.restcountries.com/countries/v5/names.common"


def get_country_data(name: str):
    headers = {"Authorization": f"Bearer {API_KEY}"}

    response = requests.get(f"{BASE_URL}/{name}", headers=headers)

    if response.status_code != 200:
        raise HTTPException(status_code=400, detail="API error")

    data = response.json()

    objects = data.get("data", {}).get("objects", [])

    if not objects:
        raise HTTPException(status_code=404, detail="Country not found")

    return objects[0]



def get_country(name: str):
    country = get_country_data(name)

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


def get_capital(name: str):
    country = get_country_data(name)
    return {"capital": country["capitals"][0]["name"]}


def get_population(name: str):
    country = get_country_data(name)
    return {"population": country["population"]}


def get_flag(name: str):
    country = get_country_data(name)
    return {"flag": country["flag"]["emoji"]}