# Отчёт о конфликтах и решениях

## Конфликт 1: формат вебхука
- Причина: разные представления тела (плоское vs envelope).
- Решение: envelope `{ event, payload }`.

## Конфликт 2: тип status
- Причина: str vs Enum.
- Решение: `TaskStatus(str, Enum)`.

## Локальные точки отказа
| Сервис               | Отказ                     | Обработка                    |
|----------------------|---------------------------|------------------------------|
| Task Service         | Notification недоступен   | 3 ретрая + failed-лог        |
| Notification Service | Некорректный payload      | 422, лог, без падения        |
| Оба                  | In-memory storage         | Потеря при рестарте (норма)  |

## E2E-тест
1. POST /api/tasks → 201.
2. Вебхук доставлен → в notifications.log строка TASK_CREATED.
3. При выключенном Notification Service Task Service пишет failed-лог.