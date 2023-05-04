from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, Mapped, mapped_column
from typing import Optional

from ..database import Base

class TypeSlot(Base):
    __tablename__ = "type_slots"
    
    id = Column(Integer, primary_key=True, index=True)
    pokemon_type_id: Mapped[int] = mapped_column(ForeignKey("types.id"))
    pokemon_type: Mapped["Type"] = relationship(back_populates="type_slots")
    slot = Column(Integer)
    
    pokemon_id: Mapped[Optional[int]] = mapped_column(ForeignKey("pokemon.id"))
    pokemon: Mapped[Optional["Pokemon"]] = relationship(back_populates="types")