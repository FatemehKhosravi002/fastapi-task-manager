from sqlalchemy.orm import Session
from . import models, schemas


def create_task(db: Session, task: schemas.TaskCreate):
    db_task = models.Task(
        title=task.title,
        description=task.description
    )
    
    db.add(db_task)
    db.commit()
    db.refresh(db_task)
    
    return db_task


def get_tasks(db: Session):
    return db.query(models.Task).all()


def get_task(db: Session, task_id: int):
    return db.query(models.Task).filter(models.Task.id == task_id).first()


def delete_task(db: Session, task_id: int):
    task = db.query(models.Task).filter(models.Task.id == task_id).first()
    
    if task:
        db.delete(task)
        db.commit()
        
    return task


def update_task(db: Session, task_id: int, updated_task: schemas.TaskUpdate):
    task = db.query(models.Task).filter(models.Task.id == task_id).first()

    if not task:
        return None

    if updated_task.title is not None:
        task.title = updated_task.title

    if updated_task.description is not None:
        task.description = updated_task.description

    if updated_task.completed is not None:
        task.completed = updated_task.completed

    db.commit()
    db.refresh(task)

    return task

