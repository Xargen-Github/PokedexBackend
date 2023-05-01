from pydantic import BaseModel

class StatBase(BaseModel):
    stat: str
    
class StatCreate(StatBase):
    pass
    
class Stat(StatBase):
    base_stat: float
    effort: float
    
    class Config:
        orm_mode = True