from fastapi import FastAPI

from app.database import engine, Base
from app import models
from app.tasks.router import router as tasks_router

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello from main!"}

@app.on_event("startup")
async def startup():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

app.include_router(tasks_router)