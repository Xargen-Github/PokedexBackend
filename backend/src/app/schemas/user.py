from pydantic import BaseModel, validator
from datetime import datetime

class UserBase(BaseModel):
    name: str
    email: str

class UserCreate(UserBase):
    password: str

class User(UserBase):
    id: int
    created_at: datetime = None
    updated_at: datetime = None
    
    class Config:
        orm_mode = True
        json_encoders = {
            datetime: lambda v: v.strftime("%m/%d/%Y, %H:%M:%S"),
        }
    