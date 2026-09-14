from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class TaskPayload(BaseModel):
    id: str
    title: str
    description: Optional[str] = None
    status: str
    created_at: datetime


class WebhookBody(BaseModel):
    event: str
    payload: TaskPayload