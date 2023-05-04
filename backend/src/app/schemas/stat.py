from pydantic import BaseModel

class StatBase(BaseModel):
    stat: str
    
class StatCreate(StatBase):
    pass
    
class Stat(StatBase):
    base_stat: float | None = None
    effort: float | None = None
    
    class Config:
        orm_mode = True