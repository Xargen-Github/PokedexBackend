from pydantic import BaseModel
from .type import TypeBase
    

class TypeSlotBase(BaseModel): 
    type: TypeBase
    slot: int
    
class TypeSlotCreate(TypeSlotBase):
    pass

class TypeSlot(TypeSlotBase):
    pass
    
    class Config:
        orm_mode = True