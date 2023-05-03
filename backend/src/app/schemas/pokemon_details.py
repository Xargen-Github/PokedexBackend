from typing import List

from .pokemon import Pokemon
from .stat import StatBase
from .ability import AbilityBase

class PokemonDetails(Pokemon):
    height: float
    weight: float
    moves: list
    order: float
    species: str
    stats: List[StatBase]
    abilities: List[AbilityBase]
    form: str
    