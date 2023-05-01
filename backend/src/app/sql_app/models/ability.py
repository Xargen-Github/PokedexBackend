from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from ..database import Base

class Ability(Base):
    __tablename__ = "abilities"
    
    id = Column(Integer, primary_key=True, index=True)
    ability = Column(String)
    is_hidden = Column(Boolean, default=False)
    slot = Column(Integer)