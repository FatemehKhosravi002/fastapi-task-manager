# FastAPI Task Manager

A simple Task Manager API built with FastAPI and PostgreSQL.

## Features

- Create tasks
- Read all tasks
- Update tasks
- Delete tasks
- PostgreSQL database integration
- SQLAlchemy ORM
- FastAPI async support

## Tech Stack

- FastAPI
- PostgreSQL
- SQLAlchemy
- Uvicorn
- Gunicorn

## Run Locally

```bash
uvicorn app.main:app --reload
```

## Run in Production

```bash
gunicorn app.main:app \
  -k uvicorn.workers.UvicornWorker \
  --workers 4 \
  --bind 0.0.0.0:8000
```

## API Endpoints

```http
GET    /tasks
POST   /tasks
PUT    /tasks/{id}
DELETE /tasks/{id}
```
