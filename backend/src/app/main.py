from fastapi import FastAPI
from models.pokemon import Pokemon

app = FastAPI()


@app.get("/api/v1/pokemons")
async def v1pokemons() -> list[Pokemon]:
    return []