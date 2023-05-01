from pydantic import BaseModel
from typing import List

from .pokemon import Pokemon
from .stat import Stat
from .ability import Ability

class PokemonDetails(Pokemon):
    height: float
    weight: float
    moves: list
    order: float
    species: str
    stats: List[Stat]
    abilities: List[Ability]
    form: str
    