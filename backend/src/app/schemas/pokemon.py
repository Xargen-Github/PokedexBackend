from pydantic import BaseModel
from typing import List

from .sprites import Sprites
from .type_slot import TypeSlot

class PokemonBase(BaseModel):
    name: str
    
class PokemonCreate(PokemonBase):
    pass

class Pokemon(PokemonBase):
    id: int
    sprites: Sprites | None = None
    types: List[TypeSlot] | None = None
    
    class Config:
        orm_mode = True