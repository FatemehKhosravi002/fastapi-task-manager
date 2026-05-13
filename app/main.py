from fastapi import FastAPI
from fastapi_swagger import patch_fastapi

from app.models import Base
from app.database import engine
from app.routers.tasks import router as task_router



Base.metadata.create_all(bind=engine)

app = FastAPI(docs_url=None, swagger_ui_oauth2_redirect_url=None)
patch_fastapi(app)


app.include_router(task_router)

