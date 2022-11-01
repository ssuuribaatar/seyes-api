# Bimon API

## Install the required packages

```sh
   poetry install
```

## Start the local server

```sh
   poetry run uvicorn app.main:app --port=3000 --reload
```

## Docker

- Build

```sh
docker build --pull --rm -f "Dockerfile" -t api "."
```

- Run

```sh
docker run --env-file .env -p 80:80 --rm -it  api:latest
```
