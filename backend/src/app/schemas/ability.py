from pydantic import BaseModel

class AbilityBase(BaseModel):
    ability: str
    
class AbilityCreate(AbilityBase):
    pass
    
class Ability(AbilityBase):
    is_hidden: bool
    slot: int
    
    class Config:
        orm_mode = True