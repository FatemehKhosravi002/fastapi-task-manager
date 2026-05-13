from pydantic import BaseModel, ConfigDict
from datetime import datetime


class TaskCreate(BaseModel):
    title: str
    description: str


class TaskResponse(BaseModel):
    id: int
    title: str
    description: str
    is_completed: bool
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)

