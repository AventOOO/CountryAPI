from fastapi import FastAPI, Query
from services import (
    get_country,
    get_country_data,
    get_capital,
    get_population,
    get_flag
)

app = FastAPI()


@app.get("/")
def root():
    return {
        "project": "CountryAPI",
        "version": "1.0",
        "author": "Макар Жуков",
        "description": "REST API for getting information about countries.",
        "available_endpoints": {
            "/country/{name}": "Get full information about a country",
            "/country/{name}/capital": "Get the capital",
            "/country/{name}/population": "Get the population",
            "/country/{name}/flag": "Get the country flag",
            "/country/{name}?fields=capital,population": "Return only selected fields"
        }
    }


@app.get("/country/{name}")
def country(
    name: str,
    fields: str | None = Query(default=None)
):
    if fields is None:
        return get_country(name)

    country = get_country_data(name)

    available_fields = {
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

    result = {}

    for field in fields.split(","):
        field = field.strip()

        if field in available_fields:
            result[field] = available_fields[field]

    return result


@app.get("/country/{name}/capital")
def capital(name: str):
    return get_capital(name)


@app.get("/country/{name}/population")
def population(name: str):
    return get_population(name)


@app.get("/country/{name}/flag")
def flag(name: str):
    return get_flag(name)