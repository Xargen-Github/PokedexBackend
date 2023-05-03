from pydantic import BaseModel
from typing import Optional

class SpritesBase(BaseModel):
    front_default: str
    
class SpritesCreate(SpritesBase):
    pass
    
class Sprites(SpritesBase):
    id: int
    front_female: str
    front_shiny: str
    front_shiny_female: str
    back_default: str
    back_female: str
    back_shiny: str
    back_shiny_female: str
    
    class Config:
        orm_mode = True