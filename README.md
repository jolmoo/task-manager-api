# 📋 Task Manager API

> RESTful API built with **FastAPI** and **PostgreSQL**, focused on clean architecture and separation of concerns.

![Python](https://img.shields.io/badge/Python-3.11+-3776AB?style=flat&logo=python&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-0.100+-009688?style=flat&logo=fastapi&logoColor=white)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-15+-4169E1?style=flat&logo=postgresql&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-ready-2496ED?style=flat&logo=docker&logoColor=white)
![License](https://img.shields.io/badge/license-MIT-green?style=flat)

---

## 📖 About

This project was built to practice backend architecture design using **FastAPI** and **PostgreSQL**. It demonstrates how to structure a backend application with a clear separation of concerns through distinct layers: router, service, and repository.

It uses **SQLAlchemy Core** (instead of the ORM) to keep full, explicit control over SQL queries.

---

## 🏗️ Architecture

The application follows a **3-layer modular architecture**:

```
HTTP Request
     │
     ▼
┌─────────────┐
│   Router    │  ← Handles HTTP, validates input/output with Pydantic
└──────┬──────┘
       │
       ▼
┌─────────────┐
│   Service   │  ← Business logic and validation rules
└──────┬──────┘
       │
       ▼
┌─────────────┐
│ Repository  │  ← SQL queries via SQLAlchemy Core
└──────┬──────┘
       │
       ▼
  PostgreSQL
```

| Layer | Responsibility |
|-------|---------------|
| **Router** | HTTP handling, Pydantic validation, response formatting |
| **Service** | Business rules, orchestration |
| **Repository** | Data access, raw SQL with SQLAlchemy Core |
| **Schemas** | Input/output DTOs via Pydantic v2 |

---

## 📁 Project Structure

```
task-manager-api/
├── app/
│   ├── main.py              # FastAPI app entry point
│   ├── database.py          # DB connection and engine setup
│   ├── routers/
│   │   └── tasks.py         # Task endpoints
│   ├── services/
│   │   └── task_service.py  # Business logic
│   ├── repositories/
│   │   └── task_repository.py  # DB queries
│   └── schemas/
│       └── task.py          # Pydantic models
├── docker/
│   └── app/
├── docker-compose.yml       # PostgreSQL local setup
├── requirements.txt
└── .env                     # Environment variables (not committed)
```

---

## 🛠️ Tech Stack

| Technology | Role |
|------------|------|
| **FastAPI** | Web framework |
| **PostgreSQL** | Relational database |
| **SQLAlchemy Core** | SQL query execution (no ORM) |
| **Pydantic v2** | Data validation and serialization |
| **Docker** | Local infrastructure |

---

## 🚦 API Endpoints

### Tasks

| Method | Endpoint | Description |
|--------|----------|-------------|
| `GET` | `/tasks` | List all tasks (supports filters) |
| `POST` | `/tasks` | Create a new task |
| `GET` | `/tasks/{task_id}` | Get a task by ID |
| `PUT` | `/tasks/{task_id}` | Update a task |
| `DELETE` | `/tasks/{task_id}` | Delete a task |
| `PATCH` | `/tasks/{task_id}/status` | Update task status |

### Filtering

Tasks can be filtered using optional query parameters:

```
GET /tasks                          → All tasks
GET /tasks?user_id=1               → Tasks by user
GET /tasks?status=done             → Tasks by status
GET /tasks?user_id=1&status=done   → Combined filters
```

### Status values

```
pending | in_progress | done
```

---

## 📦 Request & Response Examples

### Create a task

**Request:**
```http
POST /tasks
Content-Type: application/json

{
  "title": "Write unit tests",
  "description": "Cover the service layer",
  "user_id": 1,
  "status": "pending"
}
```

**Response `201 Created`:**
```json
{
  "id": 7,
  "title": "Write unit tests",
  "description": "Cover the service layer",
  "user_id": 1,
  "status": "pending",
  "created_at": "2024-11-01T10:30:00"
}
```

---

### Update task status

**Request:**
```http
PATCH /tasks/7/status?status=done
```

**Response `200 OK`:**
```json
{
  "id": 7,
  "status": "done"
}
```

---

### Task not found

**Response `404 Not Found`:**
```json
{
  "detail": "Task with id 7 not found"
}
```

---

## 🚀 Getting Started

### Prerequisites

- Python 3.11+
- Docker & Docker Compose

### 1. Clone the repository

```bash
git clone https://github.com/jolmoo/task-manager-api.git
cd task-manager-api
```

### 2. Configure environment variables

Create a `.env` file in the root directory:

```env
POSTGRES_USER=postgres
POSTGRES_PASSWORD=postgres
POSTGRES_DB=tasks_db
POSTGRES_HOST=localhost
POSTGRES_PORT=5432
```

### 3. Start the database

```bash
docker-compose up -d
```

### 4. Install dependencies and run

```bash
pip install -r requirements.txt
uvicorn app.main:app --reload
```

The API will be available at `http://localhost:8000`.

Interactive docs (Swagger UI): `http://localhost:8000/docs`

---

## 📈 Roadmap

- [ ] Authentication with JWT
- [ ] Database migrations with Alembic
- [ ] Pagination for task listing
- [ ] Unit and integration tests (pytest)
- [ ] Caching layer with Redis
- [ ] CI/CD with GitHub Actions

---

## 🎯 Learning Goals

This project was built to practice:

- Backend architecture design (layered / clean)
- Separation of concerns
- Explicit SQL-based data access with SQLAlchemy Core
- RESTful API design with FastAPI
- Local infrastructure setup with Docker

---
