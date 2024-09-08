from pydantic import BaseModel
from typing import Any, Dict


class FormSchema(BaseModel):
    id:int
    survey_id: int
    form_data: Dict[str, Any] 
    
    class Config:
        orm_mode = True

class FormCreateRequest(BaseModel):
    survey_id: int
    form_data: Dict[str, Any] 
    
    class Config:
        orm_mode = True

class FormUpdateRequest(BaseModel):
    id:int
    form_data: Dict[str, Any] 
    
    class Config:
        orm_mode = True

class FormRetrieveResponse(BaseModel):
    id: int
    survey_id: int
    form_data: Dict[str, Any] 

    class Config:
        orm_mode = True