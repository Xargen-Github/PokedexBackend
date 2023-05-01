from sqlalchemy import Boolean, Column, Float, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, Mapped
from typing import List

from ..database import Base

from pokemon import Pokemon
    
class Team(Base):
    __tablename__ = "teams"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    pokemon: Mapped[List["Pokemon"]]