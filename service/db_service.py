from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from model.task_model import Task

class PostgresDBService:
    @staticmethod
    async def get_task(db: AsyncSession, task_id: int):
        result = await db.execute(select(Task).filter(Task.id == task_id))
        return result.scalar_one_or_none()

    @staticmethod
    async def list_tasks(db: AsyncSession):
        result = await db.execute(select(Task))
        return result.scalars().all()

    @staticmethod
    async def create_task(db: AsyncSession, task_data: dict):
        task = Task(**task_data)
        db.add(task)
        await db.commit()
        await db.refresh(task)
        return task

    @staticmethod
    async def update_task(db: AsyncSession, task: Task, update_data: dict):
        for key, value in update_data.items():
            setattr(task, key, value)
        await db.commit()
        await db.refresh(task)
        return task

    @staticmethod
    async def delete_task(db: AsyncSession, task: Task):
        await db.delete(task)
        await db.commit()
        return {"message": "Task deleted successfully"}
