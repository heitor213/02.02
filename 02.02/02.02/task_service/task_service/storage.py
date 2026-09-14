from typing import Dict, List
from uuid import UUID

from models import Task


class InMemoryStorage:
    def __init__(self) -> None:
        self._tasks: Dict[UUID, Task] = {}

    def add(self, task: Task) -> Task:
        self._tasks[task.id] = task
        return task

    def list(self) -> List[Task]:
        return list(self._tasks.values())

    def clear(self) -> None:
        self._tasks.clear()


storage = InMemoryStorage()