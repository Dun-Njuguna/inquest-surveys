from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from src.models.user_survey_model import UserSurvey
from src.schemas.user_survey_schema import JoinSurveyRequest

class UserSurveyService:
    def __init__(self, db: AsyncSession):
        self.db = db

    async def join_survey(self, user_survey_data: JoinSurveyRequest) -> UserSurvey:
        user_survey = UserSurvey(**user_survey_data.dict())
        self.db.add(user_survey)
        await self.db.commit()
        await self.db.refresh(user_survey)
        return user_survey

    async def leave_survey(self, user_survey_id: int) -> None:
        user_survey = await self.get_user_survey_by_id(user_survey_id)
        if user_survey:
            await self.db.delete(user_survey)
            await self.db.commit()

    async def get_user_survey_by_id(self, user_survey_id: int) -> UserSurvey:
        result = await self.db.execute(select(UserSurvey).where(UserSurvey.id == user_survey_id))
        return result.scalar_one_or_none()
