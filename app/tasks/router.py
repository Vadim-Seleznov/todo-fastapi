from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.schemas import TaskCreate, TaskUpdate
from app.models import Task
from app.database import async_session_maker
from app.tasks.service import update_task, get_task_by_id

from sqlalchemy import select

router = APIRouter(prefix="/tasks", tags=["tasks"])

# Генератор сессии
async def get_session() -> AsyncSession:
    async with async_session_maker() as session:
        yield session

# ---------- CREATE ----------
@router.post("/")
async def create_task(data: TaskCreate, session: AsyncSession = Depends(get_session)):
    task = Task(title=data.title)
    session.add(task)
    await session.commit()
    return {
        "id": task.id,
        "title": task.title,
        "completed": task.completed,
    }

# ---------- READ ----------
@router.get("/")
async def get_tasks(session: AsyncSession = Depends(get_session)):
    result = await session.execute(select(Task))
    tasks = result.scalars().all()
    return [{"id": t.id, "title": t.title, "completed": t.completed} for t in tasks]

@router.get("/{id}")
async def get_task(id: int, session: AsyncSession = Depends(get_session)):
    task = await get_task_by_id(id, session)
    return {"id": task.id, "title": task.title, "completed": task.completed}

# ---------- UPDATE ----------
@router.patch("/{id}")
async def patch_task(id: int, data: TaskUpdate, session: AsyncSession = Depends(get_session)):
    task = await update_task(id, data, session)
    return {"id": task.id, "title": task.title, "completed": task.completed}

# ---------- DELETE ----------
@router.delete("/{id}")
async def delete_task(id: int, session: AsyncSession = Depends(get_session)):
    task = await get_task_by_id(id, session)
    await session.delete(task)
    await session.commit()
    return {"detail": f"Task {id} was successfully deleted"}
