from pydantic import BaseModel
from typing import List

from .sprites import SpritesBase
from .type_slot import TypeSlotBase

class PokemonBase(BaseModel):
    name: str
    
class PokemonCreate(PokemonBase):
    pass

class Pokemon(PokemonBase):
    id: int
    sprites: SpritesBase
    types: List[TypeSlotBase]
    
    class Config:
        orm_mode = True