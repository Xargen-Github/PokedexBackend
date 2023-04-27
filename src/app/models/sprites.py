from pydantic import BaseModel

class BaseSprites(BaseModel):
    id: int
    front_default: str
    
class Sprites(BaseSprites):
    front_female: str
    front_shiny: str
    front_shiny_female: str
    back_default: str
    back_female: str
    back_shiny: str
    back_shiny_female: str