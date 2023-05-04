from pydantic import BaseModel
from typing import List

from .version_group_detail import VersionGroupDetail

class MoveBase(BaseModel):
    move: str
    
class MoveCreate(MoveBase):
    pass

class Move(MoveBase):
    version_group_details: List[VersionGroupDetail] | None = None
    
    class Config:
        orm_mode = True