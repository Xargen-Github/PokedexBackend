from sqlalchemy import Boolean, Column, Float, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, Mapped
from typing import List

from ..database import Base

from .sprites import Sprites
from .type_slot import TypeSlot
from .move import Move
from .stat import Stat
from .ability import Ability
    
class Pokemon(Base):
    __tablename__ = "pokemon"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    sprites = Mapped["Sprites"]
    types = Mapped[List["TypeSlot"]]
    
    #Pokemon details
    height = Column(Float)
    weight = Column(Float)
    moves = Mapped[List["Move"]]
    order = Column(Float)
    species = Column(String)
    stats = Mapped[List["Stat"]]
    abilities = Mapped[List["Ability"]]
    form = Column(String)
    