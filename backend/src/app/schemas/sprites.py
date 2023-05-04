from pydantic import BaseModel
from typing import Optional

class SpritesBase(BaseModel):
    front_default: str
    
class SpritesCreate(SpritesBase):
    pass
    
class Sprites(SpritesBase):
    id: int
    front_female: str | None = None
    front_shiny: str | None = None
    front_shiny_female: str | None = None
    back_default: str | None = None
    back_female: str | None = None
    back_shiny: str | None = None
    back_shiny_female: str | None = None
    
    class Config:
        orm_mode = True