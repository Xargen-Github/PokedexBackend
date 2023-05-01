from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, Mapped

from ..database import Base
from .type import Type

class TypeSlot(Base):
    __tablename__ = "type_slots"
    
    id = Column(Integer, primary_key=True, index=True)
    type = Mapped["Type"] = relationship()