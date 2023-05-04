from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, Mapped, mapped_column
from typing import Optional

from ..database import Base

class Ability(Base):
    __tablename__ = "abilities"
    
    id = Column(Integer, primary_key=True, index=True)
    ability = Column(String)
    is_hidden = Column(Boolean, default=False, nullable=True)
    slot = Column(Integer, nullable=True)
    
    pokemon_id: Mapped[Optional[int]] = mapped_column(ForeignKey("pokemon.id"))
    pokemon: Mapped[Optional["Pokemon"]] = relationship(back_populates="abilities")