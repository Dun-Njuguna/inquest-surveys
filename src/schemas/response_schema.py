from pydantic import BaseModel
from typing import Any

class ResponseSchema(BaseModel):
    id: int
    survey_id: int
    user_id: int
    response_data: Any

    class Config:
        orm_mode = True
