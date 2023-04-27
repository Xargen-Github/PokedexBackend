# generated by fastapi-codegen:
#   filename:  openapi.yaml
#   timestamp: 2023-04-27T08:38:30+00:00

from __future__ import annotations

from typing import List, Optional, Union

from fastapi import FastAPI

from .models import (
    ApiV1TeamsIdPostRequest,
    ApiV1TeamsPostRequest,
    ApiV2PokemonsGetResponse,
    Error,
    Pokemon,
    PokemonDetails,
    Sort1,
    Sort3,
    Team,
)

app = FastAPI(
    title='Pokedex API',
    description='',
    version='1.0.0',
    contact={'name': 'Joren Vandeweyer', 'email': 'joren.vandeweyer@appwise.be'},
    servers=[{'url': 'http://localhost:3000/'}],
)


@app.get('/api/v1/pokemons', response_model=List[Pokemon], tags=['Pokemons'])
def get_api_v1_pokemons(sort: Optional[Sort1] = None) -> List[Pokemon]:
    """
    Get all pokemons
    """
    pass


@app.get(
    '/api/v1/pokemons/{id}',
    response_model=PokemonDetails,
    responses={'404': {'model': Error}},
    tags=['Pokemons'],
)
def get_api_v1_pokemons_id(id: int) -> Union[PokemonDetails, Error]:
    """
    Get a pokemon by id
    """
    pass


@app.get('/api/v1/search', response_model=List[Pokemon], tags=['Search'])
def get_api_v1_search(query: str, limit: Optional[int] = None) -> List[Pokemon]:
    """
    Search for pokemons
    """
    pass


@app.get('/api/v1/teams', response_model=List[Team], tags=['Teams'])
def get_api_v1_teams() -> List[Team]:
    """
    Get all teams
    """
    pass


@app.post(
    '/api/v1/teams',
    response_model=None,
    responses={'201': {'model': Team}},
    tags=['Teams'],
)
def post_api_v1_teams(body: ApiV1TeamsPostRequest) -> Union[None, Team]:
    """
    Create a new team
    """
    pass


@app.get(
    '/api/v1/teams/{id}',
    response_model=Team,
    responses={'404': {'model': Error}},
    tags=['Teams'],
)
def get_api_v1_teams_id(id: int) -> Union[Team, Error]:
    """
    Get a team by id
    """
    pass


@app.post(
    '/api/v1/teams/{id}',
    response_model=Team,
    responses={'404': {'model': Error}},
    tags=['Teams'],
)
def post_api_v1_teams_id(
    id: int, body: ApiV1TeamsIdPostRequest = ...
) -> Union[Team, Error]:
    """
    Set Pokemons of a team
    """
    pass


@app.get('/api/v2/pokemons', response_model=ApiV2PokemonsGetResponse, tags=['Pokemons'])
def get_api_v2_pokemons(
    sort: Optional[Sort3] = None,
    limit: Optional[int] = None,
    offset: Optional[int] = None,
) -> ApiV2PokemonsGetResponse:
    """
    Get all pokemons paginated
    """
    pass
