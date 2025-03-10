from fastapi import FastAPI
from controller.task_controller import router
from model.database import Base, engine
from contextlib import asynccontextmanager

@asynccontextmanager
async def lifespan(app: FastAPI):
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    print("App is starting") 
    yield
    print("App is stopping")  

app = FastAPI(lifespan=lifespan)
app.include_router(router)
