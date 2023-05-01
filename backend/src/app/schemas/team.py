from pydantic import BaseModel
from typing import List

from .pokemon import Pokemon


class TeamBase(BaseModel):
    name: str
    
class TeamCreate(TeamBase):
    pass

class Team(TeamBase):
    id: int
    pokemon: List[Pokemon]
    
    class Config:
        orm_mode = True