# PokedexBackend

## How to use  
Start docker containers:
```bash
docker compose up
```
Attach to the fastapi container:
```bash
docker exec -it pokedexbackend-pokedex_backend-1 /bin/bash
```
Upgrade the database:
```bash
alembic upgrade head
```
Start the api:
```bash
cd app
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```
In the browser, surf to: http://localhost:8000/docs