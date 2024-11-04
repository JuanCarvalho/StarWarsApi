# StarWarsApi

## Desafio Técnico para um processo seletivo

## Description

> Desenvolver uma API REST que retorne informações sobre os planetas e filmes do universo Star Wars.
> Utilizar Python, Flask e MongoDB.

## Usage

1. Create .env file with the following variables:

    ```
    ENV=local
    
    API_VERSION=v1
    API_HOST=0.0.0.0
    API_PORT=8000
    
    # MONGODB_HOST=mongodb
    MONGODB_HOST=localhost
    MONGODB_PORT=27017
    ```

2. Up the containers:

    ```bash
    $ docker-compose up
    ```

## Endpoints

- GET /planets
- GET /planets/id
- POST /planets
- DELETE /planets/id
- PUT /planets/id

---

- GET /movies
- GET /movies/id
- POST /movies
- DELETE /movies/id
- PUT /movies/id

## Swagger

- http://localhost:8081/

## Run linters and tests

```bash
$ cd app/
$ make
```

## Collection Postman
> Você pode importar a [StarWarsApi.postman_collection.json](./StarWarsApi.postman_collection.json) no Postman para testar todos os endpoints desta API.
