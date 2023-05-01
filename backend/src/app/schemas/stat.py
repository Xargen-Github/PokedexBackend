from pydantic import BaseModel

class Stat(BaseModel):
    stat: str
    base_stat: float
    effort: float