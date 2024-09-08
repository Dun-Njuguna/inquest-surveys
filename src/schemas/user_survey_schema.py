from pydantic import BaseModel
from typing import List, Optional

class JoinSurveyRequest(BaseModel):
    user_id: int
    survey_id: int

    class Config:
        orm_mode = True

class SubmitSurveyRequest(BaseModel):
    survey_id: int
    responses: List[dict]

    class Config:
        orm_mode = True

class LeaveSurveyRequest(BaseModel):
    survey_id: int

    class Config:
        orm_mode = True
