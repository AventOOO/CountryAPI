from fastapi import FastAPI
from services import get_country

app = FastAPI()


@app.get("/")
def home():
    return {"message": "Country API работает!"}


@app.get("/country/{name}")
def country(name: str):
    return get_country(name)