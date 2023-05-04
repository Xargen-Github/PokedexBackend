from pydantic import BaseModel
from typing import List

from .pokemon_details import PokemonDetails


class TeamBase(BaseModel):
    name: str
    
class TeamCreate(TeamBase):
    pass

class Team(TeamBase):
    id: int
    pokemon: List[PokemonDetails] | None = None
    
    class Config:
        orm_mode = True
        
class TeamUpdate(BaseModel):
    pokemon: List[int]
    