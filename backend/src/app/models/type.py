from pydantic import BaseModel

class Type(BaseModel):
    name: str
    
class TypeSlot(BaseModel):
    type: Type
    slot: int