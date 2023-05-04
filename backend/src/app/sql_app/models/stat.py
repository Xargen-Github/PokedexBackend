from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Float
from sqlalchemy.orm import relationship, Mapped, mapped_column
from typing import Optional

from ..database import Base
    
class Stat(Base):
    __tablename__ = "stats"
    
    id = Column(Integer, primary_key=True, index=True)
    stat = Column(String)
    base_stat = Column(Float, nullable=True)
    effort = Column(Float, nullable=True)
    
    pokemon_id: Mapped[Optional[int]] = mapped_column(ForeignKey("pokemon.id"))
    pokemon: Mapped[Optional["Pokemon"]] = relationship(back_populates="stats")
    