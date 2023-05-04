from sqlalchemy import Boolean, Column, Float, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, Mapped, mapped_column
from typing import List, Optional

from ..database import Base
    
class Pokemon(Base):
    __tablename__ = "pokemon"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    
    sprites_id: Mapped[Optional[int]] = mapped_column(ForeignKey("sprites.id"))
    sprites: Mapped[Optional["Sprites"]] = relationship(back_populates="pokemon")

    types: Mapped[List["TypeSlot"]] = relationship(back_populates="pokemon")
    
    #Pokemon details
    height = Column(Float, nullable=True)
    weight = Column(Float, nullable=True)
    moves: Mapped[List["Move"]] = relationship(back_populates="pokemon")
    order = Column(Float, nullable=True)
    species = Column(String, nullable=True)
    stats: Mapped[List["Stat"]] = relationship(back_populates="pokemon")
    abilities: Mapped[List["Ability"]] = relationship(back_populates="pokemon")
    form = Column(String, nullable=True)
    
    #teams: Mapped[List["Team"]] = relationship(back_populates="pokemons")
    