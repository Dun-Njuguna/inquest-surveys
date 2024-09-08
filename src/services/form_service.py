from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from src.models.form_model import Form
from src.schemas.form_schema import FormCreateRequest, FormRetrieveResponse, FormUpdateRequest

class FormService:
    def __init__(self, db: AsyncSession):
        self.db = db

    async def create_form(self, form_data: FormCreateRequest) -> Form:
        new_form = Form(**form_data.dict())
        self.db.add(new_form)
        await self.db.commit()
        await self.db.refresh(new_form)
        return new_form

    async def get_form_by_id(self, form_id: int) -> Form:
        result = await self.db.execute(select(Form).where(Form.id == form_id))
        return result.scalar_one_or_none()

    async def update_form(self, form_id: int, form_data: FormUpdateRequest) -> Form:
        form = await self.get_form_by_id(form_id)
        if form:
            for key, value in form_data.dict(exclude_unset=True).items():
                setattr(form, key, value)
            await self.db.commit()
            await self.db.refresh(form)
        return form

    async def delete_form(self, form_id: int) -> None:
        form = await self.get_form_by_id(form_id)
        if form:
            await self.db.delete(form)
            await self.db.commit()
