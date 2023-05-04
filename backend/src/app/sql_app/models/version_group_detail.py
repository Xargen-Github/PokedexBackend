from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, Mapped, mapped_column
from typing import Optional

from ..database import Base

class VersionGroupDetail(Base):
    __tablename__ = "version_group_details"
    
    id = Column(Integer, primary_key=True, index=True)
    move_learn_method = Column(String)
    version_group = Column(String)
    level_learned_at = Column(Integer)
    
    move_id: Mapped[Optional[int]] = mapped_column(ForeignKey("moves.id"))
    move: Mapped[Optional["Move"]] = relationship(back_populates="version_group_details")