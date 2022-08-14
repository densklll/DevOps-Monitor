# Техническая документация для проекта DevOps Monitor

## 1. Архитектура проекта
- **Backend**:
  - Разработан на Django с использованием Django REST Framework.
  - Модели: Pipeline, Build, Notification, CISystemIntegration.
  - Интеграция с внешними системами (Jenkins, GitHub Actions, GitLab CI) через REST API.
- **Frontend**:
  - Реализован на React, используется Material-UI для оформления и Recharts для визуализации.
- **Контейнеризация**:
  - Dockerfile для Backend и Frontend.
  - docker-compose для локальной разработки.
  - Kubernetes манифесты для продакшена.

## 2. Интеграция компонентов
- **API документация**:
  - Используется drf-yasg для генерации Swagger документации.
  - Доступна по URL: `/swagger/` и `/redoc/`.
- **CI/CD**: 
  - Автоматизированный пайплайн на GitHub Actions описан в `.github/workflows/ci.yml`.

## 3. Безопасность и оптимизация
- Проведен предварительный аудит безопасности:
  - Используются меры защиты от SQL-инъекций, CSRF, XSS.
  - Рекомендуется запуск статического анализа через Bandit и ESLint.
- Логирование ошибок настраивается через Sentry.
- Оптимизация запросов к базе данных через select_related, prefetch_related, индексы.

## 4. Развертывание
- **Локальное окружение**: Docker-compose.
- **Продакшн**: Kubernetes манифесты (Deployment, Service, Ingress).
- Настройка производится через переменные окружения.

## 5. Руководство для разработчиков
- **Структура проекта**:
  - Backend: директория `backend/`
  - Frontend: директория `frontend/`
  - Документация: директория `docs/`
- **Процесс разработки**:
  - Внесение изменений производится с соблюдением CI/CD процессов.
  - Запуск тестов перед деплоем.
  - Использование Git для контроля версий. 
## 2022-01-23
Mark CI layout verify step scope (CI runner)

## 2022-02-09
Document serializer null owner edge case (demo box)

## 2022-02-26
Clarify Ingress TLS and default certificate (prod checklist)

## 2022-03-17
Adjust integration service timeout budget (demo box)

## 2022-04-08
Review CI layout verify step scope (demo box)

## 2022-05-01
Describe notification retry semantics (CI runner)

## 2022-05-18
Review Compose dependency boot order (staging)

## 2022-05-29
Stub Locust hatch rate on laptop (local dev)

## 2022-06-19
Describe settings module env toggles (local dev)

## 2022-07-11
Clarify Compose dependency boot order (staging)

## 2022-08-02
Record pytest isolation for pipeline models (CI runner)

## 2022-08-14
Capture CI layout verify step scope (local dev)
