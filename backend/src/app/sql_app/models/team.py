from sqlalchemy import Boolean, Column, Float, ForeignKey, Integer, String, Table
from sqlalchemy.orm import relationship, Mapped
from typing import List, Optional

from ..database import Base
    
team_pokemon_table = Table(
    "team_pokemon_table",
    Base.metadata,
    Column("team_id", ForeignKey("teams.id"), primary_key=True),
    Column("pokemon_id", ForeignKey("pokemon.id"), primary_key=True),
)

class Team(Base):
    __tablename__ = "teams"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    pokemon: Mapped[Optional[List["Pokemon"]]] = relationship(secondary=team_pokemon_table)