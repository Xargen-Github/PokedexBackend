from typing import List

from .pokemon import Pokemon
from .stat import Stat
from .ability import Ability
from .move import Move

class PokemonDetails(Pokemon):
    height: float | None = None
    weight: float | None = None
    moves: List[Move] | None = None
    order: float | None = None
    species: str | None = None
    stats: List[Stat] | None = None
    abilities: List[Ability] | None = None
    form: str | None = None
    