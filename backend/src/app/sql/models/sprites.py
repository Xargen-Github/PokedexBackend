from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from ..database import Base

class BaseSprites(BaseModel):
    id: int
    front_default: str
    
class Sprites(Base):
    __tablename__ = "sprites"
    
    id = Column(Integer, primary_key=True, index=True)
    front_default = Column(String)
    front_female = Column(String)
    front_shiny = Column(String)
    front_shiny_female = Column(String)
    back_default = Column(String)
    back_female = Column(String)
    back_shiny = Column(String)
    back_shiny_female = Column(String)