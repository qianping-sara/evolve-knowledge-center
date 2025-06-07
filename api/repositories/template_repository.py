from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from api.models.template_model import Template

class TemplateRepository:
    @staticmethod
    async def create(db: AsyncSession, obj: Template):
        db.add(obj)
        await db.commit()
        await db.refresh(obj)
        return obj

    @staticmethod
    async def get(db: AsyncSession, template_id: str):
        result = await db.execute(select(Template).where(Template.id == template_id))
        return result.scalar_one_or_none()

    @staticmethod
    async def list(db: AsyncSession):
        result = await db.execute(select(Template))
        return result.scalars().all()

    @staticmethod
    async def update(db: AsyncSession, obj: Template):
        await db.commit()
        await db.refresh(obj)
        return obj

    @staticmethod
    async def delete(db: AsyncSession, obj: Template):
        await db.delete(obj)
        await db.commit() 