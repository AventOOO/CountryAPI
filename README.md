# CountryAPI

REST API application developed with FastAPI.

## Description

This project uses the REST Countries API v5 to retrieve information about countries.

The application allows users to:

- Get full information about a country.
- Get the capital city.
- Get the population.
- Get the country flag.
- Return only selected fields using query parameters.

## Technologies

- Python 3.13
- FastAPI
- Requests
- Uvicorn
- Git

## Installation

Clone the repository.

```bash
git clone <repository_url>
```

Install dependencies.

```bash
pip install -r requirements.txt
```

Run the server.

```bash
uvicorn main:app --reload
```

## Endpoints

### Get full information

```
GET /country/{name}
```

Example:

```
GET /country/japan
```

### Get capital

```
GET /country/{name}/capital
```

### Get population

```
GET /country/{name}/population
```

### Get flag

```
GET /country/{name}/flag
```

### Filter fields

```
GET /country/{name}?fields=capital,population
```

## Author

Makar Zhukov