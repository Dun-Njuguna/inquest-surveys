from fastapi import APIRouter, HTTPException, Depends
from fastapi.responses import JSONResponse
from sqlalchemy.ext.asyncio import AsyncSession
from src.services.form_service import FormService
from src.env.database import get_db
from src.schemas.form_schema import FormCreateRequest, FormRetrieveResponse

router = APIRouter()

@router.post("/add")
async def generate_form(request: FormCreateRequest, db: AsyncSession = Depends(get_db)):
    try:
        service = FormService(db)
        result = await service.generate_form(request.title, request.fields)
        return JSONResponse(content={"error": False, "message": "Form generated successfully", "data": result})
    except Exception as e:
        return JSONResponse(content={"error": True, "message": str(e), "data": None}, status_code=400)

@router.get("/{form_id}")
async def get_form(form_id: int, db: AsyncSession = Depends(get_db)):
    try:
        service = FormService(db)
        form = await service.get_form(form_id)
        if not form:
            raise HTTPException(status_code=404, detail="Form not found")
        return JSONResponse(content={"error": False, "message": "Form retrieved successfully", "data": form})
    except Exception as e:
        return JSONResponse(content={"error": True, "message": str(e), "data": None}, status_code=400)
