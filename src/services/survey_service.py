from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from src.models.survey_model import Survey
from src.schemas.survey_schema import SurveyCreate, SurveyUpdate

class SurveyService:
    def __init__(self, db: AsyncSession):
        self.db = db

    async def create_survey(self, survey_data: SurveyCreate) -> Survey:
        new_survey = Survey(**survey_data.dict())
        self.db.add(new_survey)
        await self.db.commit()
        await self.db.refresh(new_survey)
        return new_survey

    async def get_survey_by_id(self, survey_id: int) -> Survey:
        result = await self.db.execute(select(Survey).where(Survey.id == survey_id))
        return result.scalar_one_or_none()

    async def update_survey(self, survey_id: int, survey_data: SurveyUpdate) -> Survey:
        survey = await self.get_survey_by_id(survey_id)
        if survey:
            for key, value in survey_data.dict(exclude_unset=True).items():
                setattr(survey, key, value)
            await self.db.commit()
            await self.db.refresh(survey)
        return survey

    async def delete_survey(self, survey_id: int) -> None:
        survey = await self.get_survey_by_id(survey_id)
        if survey:
            await self.db.delete(survey)
            await self.db.commit()
