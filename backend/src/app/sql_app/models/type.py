from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.orm import relationship, Mapped
from typing import List

from ..database import Base
    
class Type(Base):
    __tablename__ = "types"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    
    type_slots: Mapped[List["TypeSlot"]] = relationship(back_populates="pokemon_type")