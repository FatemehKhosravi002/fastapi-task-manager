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

