from pydantic import BaseModel
from typing import List

from sprites import Sprites
from type_slot import TypeSlot

class Pokemon(BaseModel):
    id: int
    name: str
    sprites: Sprites
    types: List[TypeSlot]