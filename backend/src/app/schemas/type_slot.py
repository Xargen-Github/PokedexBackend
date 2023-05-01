from pydantic import BaseModel
from .type import Type
    
class TypeSlot(BaseModel):
    type: Type
    slot: int