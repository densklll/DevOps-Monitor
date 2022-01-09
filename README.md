# DevOps Monitor

[![CI/CD Pipeline](https://github.com/densklll/DevOps-Monitor/actions/workflows/ci.yml/badge.svg)](https://github.com/densklll/DevOps-Monitor/actions/workflows/ci.yml)
[![Docker Compose](https://img.shields.io/badge/Compose-3.8-2496ED?logo=docker&logoColor=white)](https://docs.docker.com/compose/)
[![Kubernetes](https://img.shields.io/badge/Kubernetes-Manifests-326CE5?logo=kubernetes&logoColor=white)](https://kubernetes.io/)
[![Python](https://img.shields.io/badge/Python-3.9-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![Node](https://img.shields.io/badge/Node.js-14-339933?logo=nodedotjs&logoColor=white)](https://nodejs.org/)

Reference layout for a **CI/CD monitoring** style platform: Docker Compose for local stacks, **Kubernetes** manifests, a **Django-oriented** `ci` service package (models, API views, notifications, analytics helpers), sample backend tests, **Locust** load-test entrypoint, and a **GitHub Actions** workflow.

---

## What’s in the repo

| Area | Contents |
|------|----------|
| **`ci/`** | Django-style app code: models, serializers, views, URLs, notification and analytics helpers |
| **`backend/tests/`** | Sample API/model tests (expect a wired Django project to run them) |
| **`frontend/`** | Dockerfile scaffold; `cypress/` for UI tests |
| **`k8s/`** | Kubernetes deployment assets |
| **`docs/`** | Technical notes |
| **Root** | `docker-compose.yml` (Postgres, Redis, backend/frontend services), `locustfile.py`, `settings.py` |

## Features (target architecture)

- Build/pipeline concepts modeled in `ci` (pipelines, builds, integrations, notifications)
- Notifications (email / Slack / Telegram) and analytics helpers in code layout
- **Swagger** wiring example: `backend/swagger_urls.py`
- **Containerized** backend and frontend; **Compose** orchestration with Postgres and Redis
- **CI** automation via GitHub Actions (repository layout validation)
- **Load testing** entry via Locust (`locustfile.py`)

## Quick start

```bash
git clone https://github.com/densklll/DevOps-Monitor.git
cd DevOps-Monitor
```

Copy environment variables you need into a `.env` file (see example below), then:

```bash
docker compose up --build
```

Expected service ports from `docker-compose.yml`:

| Service | URL |
|---------|-----|
| Backend | [http://localhost:8000](http://localhost:8000) |
| Frontend | [http://localhost:3000](http://localhost:3000) |
| Postgres | `localhost:5432` |
| Redis | `localhost:6379` |

### Example `.env`

```bash
DEBUG=1
DJANGO_ALLOWED_HOSTS=localhost,127.0.0.1
DATABASE_URL=postgres://postgres:postgres@db:5432/devops_monitor
REDIS_URL=redis://redis:6379/0
SMTP_HOST=smtp.example.com
SMTP_PORT=587
SMTP_USERNAME=you@example.com
SMTP_PASSWORD=secret
SLACK_WEBHOOK_URL=https://hooks.slack.com/services/...
TELEGRAM_BOT_TOKEN=your_bot_token
TELEGRAM_CHAT_ID=your_chat_id
```

## API docs (when Django is wired)

- Swagger: `http://localhost:8000/swagger/`
- Redoc: `http://localhost:8000/redoc/`

## Testing & tooling

- **Backend**: connect a full Django project (`manage.py`, `requirements.txt`) to run `backend/tests` with `python manage.py test`
- **Frontend / E2E**: `cd frontend && npx cypress open` when a React app is present
- **Load tests**: `locust --host=http://localhost:8000` then open [http://localhost:8089](http://localhost:8089)

## Kubernetes

Apply manifests under `k8s/` for your cluster and registry (adjust images and secrets).

## Contributing

Issues and pull requests are welcome.
