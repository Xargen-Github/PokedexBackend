from pydantic import BaseModel
from .type import Type
    

class TypeSlotBase(BaseModel): 
    type: Type
    slot: int
    
class TypeSlotCreate(TypeSlotBase):
    pass

class TypeSlot(TypeSlotBase):
    pass
    
    class Config:
        orm_mode = True