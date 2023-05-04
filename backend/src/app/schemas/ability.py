from pydantic import BaseModel

class AbilityBase(BaseModel):
    ability: str
    
class AbilityCreate(AbilityBase):
    pass
    
class Ability(AbilityBase):
    is_hidden: bool | None = None
    slot: int | None = None
    
    class Config:
        orm_mode = True