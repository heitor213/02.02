import asyncio
import logging
from pathlib import Path

import httpx

from config import (
    FAILED_WEBHOOKS_LOG,
    MAX_RETRIES,
    NOTIFICATION_URL,
    REQUEST_TIMEOUT,
    RETRY_BASE_DELAY,
)
from models import Task, WebhookPayload

logger = logging.getLogger("task_service.webhook")


async def send_task_created(task: Task) -> bool:
    payload = WebhookPayload(payload=task).model_dump(mode="json")

    for attempt in range(1, MAX_RETRIES + 1):
        try:
            async with httpx.AsyncClient(timeout=REQUEST_TIMEOUT) as client:
                r = await client.post(NOTIFICATION_URL, json=payload)
                if r.status_code == 200:
                    logger.info("Webhook delivered for task %s", task.id)
                    return True
                logger.warning("Attempt %s: status %s", attempt, r.status_code)
        except Exception as exc:  # noqa: BLE001
            logger.warning("Attempt %s error: %s", attempt, exc)

        await asyncio.sleep(RETRY_BASE_DELAY * 2 ** (attempt - 1))

    Path(FAILED_WEBHOOKS_LOG).parent.mkdir(parents=True, exist_ok=True)
    with open(FAILED_WEBHOOKS_LOG, "a", encoding="utf-8") as f:
        f.write(f"{task.id}\t{task.model_dump_json()}\n")
    logger.error("Webhook permanently failed for task %s", task.id)
    return False