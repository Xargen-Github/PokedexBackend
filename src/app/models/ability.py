from pydantic import BaseModel

class Ability(BaseModel):
    ability: str
    is_hidden: bool
    slot: int