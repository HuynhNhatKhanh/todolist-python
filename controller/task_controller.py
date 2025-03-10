from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from service.db_service import PostgresDBService
from model.database import get_db
from service.kafka_producer import send_message

router = APIRouter()

@router.get("/")
async def root():
    return {"message": "Hello World"}

@router.post("/task")
async def create_task(task_data: dict):
    await send_message({"event": "task_created", "data": task_data})
    return {"message": "Task sent to Kafka", "task": task_data}

@router.get("/task/{task_id}")
async def get_task(task_id: int, db: AsyncSession = Depends(get_db)):
    task = await PostgresDBService.get_task(db, task_id)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    return task

@router.get("/task")
async def list_tasks(db: AsyncSession = Depends(get_db)):
    tasks = await PostgresDBService.list_tasks(db)
    return tasks if tasks else []

@router.put("/task/{task_id}")
async def update_task(task_id: int, update_data: dict, db: AsyncSession = Depends(get_db)):
    update_data["id"] = task_id
    await send_message({"event": "task_updated", "data": update_data})
    return {"message": "Task sent to Kafka", "task": update_data}

@router.delete("/task/{task_id}")
async def delete_task(task_id: int, db: AsyncSession = Depends(get_db)):
    task = await PostgresDBService.get_task(db, task_id)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    return await PostgresDBService.delete_task(db, task)
