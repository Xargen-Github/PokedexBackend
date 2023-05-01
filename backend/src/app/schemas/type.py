from pydantic import BaseModel

class TypeBase(BaseModel):
    name: str
    
class TypeCreate(TypeBase):
    pass

class Type(TypeBase):
    pass
    
    class Config:
        orm_mode = True