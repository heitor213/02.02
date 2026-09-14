# Smart Task Planner

Прототип сервиса «Умный планировщик задач» — два микросервиса,
взаимодействующих через HTTP-вебхук.

## Состав
- **Task Service** (порт 8000) — CRUD задач.
- **Notification Service** (порт 8001) — приём событий и логирование.

## Установка
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

## Запуск
# Терминал 1
cd task_service && uvicorn main:app --reload --port 8000

# Терминал 2
cd notification_service && uvicorn main:app --reload --port 8001

## Проверка
curl -X POST http://localhost:8000/api/tasks \
  -H "Content-Type: application/json" \
  -d '{"title":"Купить молоко","description":"2 литра"}'

## Тесты
pytest task_service -v
pytest notification_service -v