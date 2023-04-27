from pydantic import BaseModel
from typing import List

from version_group_details import VersionGroupDetail

class Move(BaseModel):
    move: str
    version_group_details: List[VersionGroupDetail]