from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from src.env.database import get_db
from src.services.survey_service import SurveyService
from src.schemas.survey_schema import SurveyCreate, SurveyUpdate, SurveyResponse
from src.utils.dependencies import get_current_user

router = APIRouter()

@router.post("/surveys", response_model=SurveyResponse)
async def create_survey(
    survey: SurveyCreate, 
    db: AsyncSession = Depends(get_db), 
    current_user: dict = Depends(get_current_user)
):
    survey_service = SurveyService(db)
    created_survey = await survey_service.create_survey(survey, current_user['id'])
    return created_survey

@router.put("/surveys/{survey_id}", response_model=SurveyResponse)
async def update_survey(
    survey_id: int, 
    survey: SurveyUpdate, 
    db: AsyncSession = Depends(get_db), 
    current_user: dict = Depends(get_current_user)
):
    survey_service = SurveyService(db)
    updated_survey = await survey_service.update_survey(survey_id, survey, current_user['id'])
    if not updated_survey:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Survey not found")
    return updated_survey

@router.delete("/surveys/{survey_id}", response_model=dict)
async def delete_survey(
    survey_id: int, 
    db: AsyncSession = Depends(get_db), 
    current_user: dict = Depends(get_current_user)
):
    survey_service = SurveyService(db)
    deleted = await survey_service.delete_survey(survey_id, current_user['id'])
    if not deleted:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Survey not found")
    return {"detail": "Survey deleted successfully"}
