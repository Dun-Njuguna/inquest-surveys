from pydantic import BaseModel
from typing import Any, Dict, List, Optional, Union

class ResponseModel(BaseModel):
    error: bool  # Indicates if there was an error
    message: str  # A message describing the result or error
    data: Optional[Union[Dict[str, Any], List[Any]]]  # Data can be a dictionary or a list; it is optional

    class Config:
        from_attributes = True  # Allows the model to create instances from attributes directly
