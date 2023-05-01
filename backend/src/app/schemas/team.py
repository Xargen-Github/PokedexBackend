from pydantic import BaseModel
from typing import List

from .pokemon import Pokemon

class Team(BaseModel):
    id: int
    name: str
    pokemon: List[Pokemon]