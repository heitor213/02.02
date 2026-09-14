import logging

from fastapi import BackgroundTasks, FastAPI

from models import Task, TaskCreate
from storage import storage
from webhook import send_task_created

logging.basicConfig(level=logging.INFO)

app = FastAPI(title="Task Service", version="1.0.0")


@app.post("/api/tasks", response_model=Task, status_code=201)
async def create_task(payload: TaskCreate, background: BackgroundTasks):
    task = Task.from_create(payload)
    storage.add(task)
    background.add_task(send_task_created, task)
    return task


@app.get("/api/tasks", response_model=list[Task])
async def list_tasks():
    return storage.list()


@app.get("/health")
async def health():
    return {"status": "ok"}