from fastapi import FastAPI
from services import get_country, get_country_data

app = FastAPI()


@app.get("/")
def root():
    return {"message": "Country API"}


@app.get("/country/{name}")
def country(name: str):
    return get_country(name)


@app.get("/country/{name}/capital")
def capital(name: str):
    country = get_country_data(name)
    return {
        "country": country["names"]["common"],
        "capital": country["capitals"][0]["name"]
    }


@app.get("/country/{name}/population")
def population(name: str):
    country = get_country_data(name)
    return {
        "country": country["names"]["common"],
        "population": country["population"]
    }


@app.get("/country/{name}/flag")
def flag(name: str):
    country = get_country_data(name)
    return {
        "country": country["names"]["common"],
        "flag": country["flag"]["emoji"]
    }