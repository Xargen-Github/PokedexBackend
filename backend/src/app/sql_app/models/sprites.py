from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, Mapped, mapped_column

from ..database import Base
    
class Sprites(Base):
    __tablename__ = "sprites"
    
    id = Column(Integer, primary_key=True, index=True)
    front_default = Column(String)
    
    front_female = Column(String, nullable=True)
    front_shiny = Column(String, nullable=True)
    front_shiny_female = Column(String, nullable=True)
    back_default = Column(String, nullable=True)
    back_female = Column(String, nullable=True)
    back_shiny = Column(String, nullable=True)
    back_shiny_female = Column(String, nullable=True)
    
    pokemon: Mapped["Pokemon"] = relationship(back_populates="sprites")