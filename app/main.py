from fastapi import FastAPI

from app.models import Base
from app.database import engine
from routers.tasks import router as task_router


Base.metadata.create_all(bind=engine)

app = FastAPI()


app.include_router(task_router)

