from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, Mapped
from typing import List

from ..database import Base
  
class Move(Base):
    __tablename__ = "moves"
    
    id = Column(Integer, primary_key=True, index=True)
    move = Column(String)
    version_group_details: Mapped[List["VersionGroupDetail"]] = relationship(back_populates="move")