from fastapi import APIRouter, HTTPException, Depends, Request
from fastapi.responses import JSONResponse
from sqlalchemy.ext.asyncio import AsyncSession
from src.services.user_survey_service import UserSurveyService
from src.utils.dependencies import get_current_user
from src.env.database import get_db
from src.schemas.user_survey_schema import JoinSurveyRequest, SubmitSurveyRequest, LeaveSurveyRequest

router = APIRouter()

@router.post("/join")
async def join_survey(request: JoinSurveyRequest, db: AsyncSession = Depends(get_db), user: dict = Depends(get_current_user)):
    try:
        service = UserSurveyService(db)
        result = await service.join_survey(user['id'], request.survey_id)
        return JSONResponse(content={"error": False, "message": "Successfully joined the survey", "data": result})
    except Exception as e:
        return JSONResponse(content={"error": True, "message": str(e), "data": None}, status_code=400)

@router.post("/submit")
async def submit_survey(request: SubmitSurveyRequest, db: AsyncSession = Depends(get_db), user: dict = Depends(get_current_user)):
    try:
        service = UserSurveyService(db)
        result = await service.submit_survey(user['id'], request.survey_id, request.responses)
        return JSONResponse(content={"error": False, "message": "Survey submitted successfully", "data": result})
    except Exception as e:
        return JSONResponse(content={"error": True, "message": str(e), "data": None}, status_code=400)

@router.post("/leave")
async def leave_survey(request: LeaveSurveyRequest, db: AsyncSession = Depends(get_db), user: dict = Depends(get_current_user)):
    try:
        service = UserSurveyService(db)
        result = await service.leave_survey(user['id'], request.survey_id)
        return JSONResponse(content={"error": False, "message": "Successfully left the survey", "data": result})
    except Exception as e:
        return JSONResponse(content={"error": True, "message": str(e), "data": None}, status_code=400)
