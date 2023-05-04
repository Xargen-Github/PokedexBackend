from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, Mapped, mapped_column
from typing import List, Optional

from ..database import Base
  
class Move(Base):
    __tablename__ = "moves"
    
    id = Column(Integer, primary_key=True, index=True)
    move = Column(String)
    version_group_details: Mapped[List["VersionGroupDetail"]] = relationship(back_populates="move")
    
    pokemon_id: Mapped[Optional[int]] = mapped_column(ForeignKey("pokemon.id"))
    pokemon: Mapped[Optional["Pokemon"]] = relationship(back_populates="moves")