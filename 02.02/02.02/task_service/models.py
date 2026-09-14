from datetime import datetime
from enum import Enum
from typing import Optional
from uuid import UUID, uuid4

from pydantic import BaseModel, Field


class TaskStatus(str, Enum):
    new = "new"
    in_progress = "in_progress"
    done = "done"


class TaskCreate(BaseModel):
    title: str = Field(..., min_length=1, max_length=200)
    description: Optional[str] = Field(None, max_length=2000)
    status: TaskStatus = TaskStatus.new


class Task(BaseModel):
    id: UUID
    title: str
    description: Optional[str] = None
    status: TaskStatus = TaskStatus.new
    created_at: datetime

    @classmethod
    def from_create(cls, data: TaskCreate) -> "Task":
        return cls(
            id=uuid4(),
            title=data.title,
            description=data.description,
            status=data.status,
            created_at=datetime.utcnow(),
        )


class WebhookPayload(BaseModel):
    event: str = "task_created"
    payload: Task