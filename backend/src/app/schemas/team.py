from pydantic import BaseModel
from typing import List

from .pokemon import PokemonBase


class TeamBase(BaseModel):
    name: str
    
class TeamCreate(TeamBase):
    pass

class Team(TeamBase):
    id: int
    pokemon: List[PokemonBase]
    
    class Config:
        orm_mode = True