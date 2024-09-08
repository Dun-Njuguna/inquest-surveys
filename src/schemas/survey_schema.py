from pydantic import BaseModel
from typing import Optional, List
from src.schemas.form_schema import FormSchema
from src.schemas.response_schema import ResponseSchema

class SurveyCreate(BaseModel):
    title: str
    description: Optional[str] = None

class SurveyUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    is_active: Optional[bool] = None

class SurveyResponse(BaseModel):
    id: int
    title: str
    description: Optional[str] = None
    is_active: bool
    forms: List[FormSchema] = []
    responses: List[ResponseSchema] = []

    class Config:
        orm_mode = True
