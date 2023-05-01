from pydantic import BaseModel

class VersionGroupDetail(BaseModel):
    move_learn_method: str
    version_group: str
    level_learned_at: int