# 🚀 Task Management API | Modular Clean Architecture

A RESTful API built with FastAPI and PostgreSQL, designed with a focus on separation of concerns and modular architecture.

This project demonstrates how to structure a backend application using clear layers (router, service, repository) and direct SQL queries with SQLAlchemy Core.

---

## 🏗️ Architecture

The system follows a modular layered architecture:

### Layers Overview

* **Transport Layer (Routers)**
  Handles HTTP requests, validation with Pydantic, and response formatting.

* **Service Layer (Business Logic)**
  Contains validation rules and orchestrates application logic.

* **Repository Layer (Data Access)**
  Executes SQL queries using SQLAlchemy Core, keeping full control over database interactions.

* **Schemas (DTOs)**
  Define input/output validation using Pydantic models.

---

## 🛠️ Tech Stack

| Technology      | Role                 |
| --------------- | -------------------- |
| FastAPI         | Web framework        |
| PostgreSQL      | Relational database  |
| SQLAlchemy Core | SQL query execution  |
| Pydantic v2     | Data validation      |
| Docker          | Local infrastructure |

---

## 🚦 Features

### Task Filtering

Dynamic filtering with optional query parameters:

```bash
GET /tasks
GET /tasks?user_id=1
GET /tasks?status=done
GET /tasks?user_id=1&status=done
```

---

### Task Status Management

Dedicated endpoint for updating task state:

```bash
PATCH /tasks/{task_id}/status?status=done
```

---

## 🚀 Getting Started

### 1. Start database

```bash
docker-compose up -d
```

### 2. Configure environment

Create a `.env` file:

```ini
POSTGRES_USER=postgres
POSTGRES_PASSWORD=postgres
POSTGRES_DB=tasks_db
POSTGRES_HOST=localhost
POSTGRES_PORT=5432
```

---

### 3. Run the API

```bash
pip install -r requirements.txt
uvicorn app.main:app --reload
```

---

## 📈 Future Improvements

* Add authentication (JWT)
* Introduce database migrations (Alembic)
* Implement pagination
* Add caching layer (Redis)
* Add automated tests

---

## 👨‍💻 Purpose

This project was built to practice:

* backend architecture design
* separation of concerns
* SQL-based data access
* API design with FastAPI
