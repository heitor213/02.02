from fastapi import FastAPI

from logger import logger
from models import WebhookBody

app = FastAPI(title="Notification Service", version="1.0.0")


@app.post("/api/webhooks/task_created")
async def task_created(body: WebhookBody):
    logger.info(
        "TASK_CREATED | id=%s | title=%r | status=%s | created_at=%s",
        body.payload.id,
        body.payload.title,
        body.payload.status,
        body.payload.created_at.isoformat(),
    )
    return {"status": "received"}


@app.get("/health")
async def health():
    return {"status": "ok"}