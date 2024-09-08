from typing import Optional
from pydantic import BaseModel, EmailStr

class UserSchema(BaseModel):
    id: str
    email: EmailStr
    username: str
    role: Optional[str] = None
    
    class Config:
        from_attributes = True

