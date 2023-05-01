from pydantic import BaseModel

class VersionGroupDetailBase(BaseModel):
    move_learn_method: str
    version_group: str
    level_learned_at: int

class VersionGroupDetailCreate(VersionGroupDetailBase):
    pass

class VersionGroupDetail(VersionGroupDetailBase):
    pass
    
    class Config:
        orm_mode = True