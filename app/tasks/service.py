from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import HTTPException

from app.models import Task
from app.schemas import TaskUpdate

async def get_task_by_id(task_id: int, session: AsyncSession) -> Task:
    result = await session.execute(select(Task).where(Task.id == task_id))
    task = result.scalar_one_or_none()
    if not task:
        raise HTTPException(status_code=404, detail=f"Task not found at id: {task_id}")
    return task

async def update_task(task_id: int, data: TaskUpdate, session: AsyncSession) -> Task:
    task = await get_task_by_id(task_id, session)
    if data.title is not None:
        task.title = data.title
    if data.completed is not None:
        task.completed = data.completed
    await session.commit()
    return task
