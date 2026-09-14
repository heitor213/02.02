# API Contract — Smart Task Planner (v1.0.0)

## 1. Схема данных Task
| Поле        | Тип     | Обяз. | Описание                       |
|-------------|---------|-------|--------------------------------|
| id          | UUID    | auto  | Идентификатор                  |
| title       | string  | да    | 1–200 символов                 |
| description | string  | нет   | до 2000 символов               |
| status      | enum    | да    | new / in_progress / done       |
| created_at  | ISO8601 | auto  | UTC                            |

## 2. Task Service

### POST /api/tasks → 201
Request:
{ "title": "Купить молоко", "description": "2 литра", "status": "new" }

Response:
{
  "id": "3f1c...",
  "title": "Купить молоко",
  "description": "2 литра",
  "status": "new",
  "created_at": "2026-09-14T10:00:00Z"
}

### GET /api/tasks → 200
[{ ...Task... }]

## 3. Notification Service

### POST /api/webhooks/task_created → 200
Request:
{
  "event": "task_created",
  "payload": { ...Task... }
}

Response:
{ "status": "received" }

## 4. Гарантии доставки
- Асинхронная отправка (BackgroundTasks).
- 3 ретрая: 0.5s → 1s → 2s.
- При неудаче — лог `task_service_failed_webhooks.log`.