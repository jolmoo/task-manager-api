from sqlalchemy import text
from sqlalchemy.orm import Session


def create_task(db: Session, title: str, description: str | None, user_id: int):
    query = text("""
        INSERT INTO tasks (title, description, user_id)
        VALUES (:title, :description, :user_id)
        RETURNING id, title, description, user_id, status
    """)

    result = db.execute(
        query,
        {
            "title": title,
            "description": description,
            "user_id": user_id,
        },
    )
    row = result.fetchone()
    db.commit()

    return {
        "id": row.id,
        "title": row.title,
        "description": row.description,
        "user_id": row.user_id,
        "status": row.status,
    }


def get_tasks_by_user_id(db: Session, user_id: int):
    query = text("""
        SELECT id, title, description, user_id, status
        FROM tasks
        WHERE user_id = :user_id
        ORDER BY id
    """)

    result = db.execute(query, {"user_id": user_id})
    rows = result.fetchall()

    return [
        {
            "id": row.id,
            "title": row.title,
            "description": row.description,
            "user_id": row.user_id,
            "status": row.status,
        }
        for row in rows
    ]


def get_task_by_id(db: Session, task_id: int):
    query = text("""
        SELECT id, title, description, user_id, status
        FROM tasks
        WHERE id = :task_id
    """)

    result = db.execute(query, {"task_id": task_id})
    row = result.fetchone()

    if row is None:
        return None

    return {
        "id": row.id,
        "title": row.title,
        "description": row.description,
        "user_id": row.user_id,
        "status": row.status,
    }


def get_all_tasks(db: Session):
    query = text("""
        SELECT id, title, description, user_id, status
        FROM tasks
        ORDER BY id
    """)

    result = db.execute(query)
    rows = result.fetchall()

    return [
        {
            "id": row.id,
            "title": row.title,
            "description": row.description,
            "user_id": row.user_id,
            "status": row.status,
        }
        for row in rows
    ]


def delete_task_by_id(db: Session, task_id: int):
    query = text("""
        DELETE FROM tasks
        WHERE id = :task_id
        RETURNING id
    """)

    result = db.execute(query, {"task_id": task_id})
    row = result.fetchone()
    db.commit()

    if row is None:
        return None

    return row.id


def update_task_by_id(
    db: Session,
    task_id: int,
    title: str,
    description: str | None,
    user_id: int,
):
    query = text("""
        UPDATE tasks
        SET title = :title,
            description = :description,
            user_id = :user_id
        WHERE id = :task_id
        RETURNING id, title, description, user_id, status
    """)

    result = db.execute(
        query,
        {
            "task_id": task_id,
            "title": title,
            "description": description,
            "user_id": user_id,
        },
    )

    row = result.fetchone()
    db.commit()

    if row is None:
        return None

    return {
        "id": row.id,
        "title": row.title,
        "description": row.description,
        "user_id": row.user_id,
        "status": row.status,
    }


def update_task_status(db: Session, task_id: int, status: str):
    query = text("""
        UPDATE tasks
        SET status = :status
        WHERE id = :task_id
        RETURNING id, title, description, user_id, status
    """)

    result = db.execute(
        query,
        {
            "task_id": task_id,
            "status": status,
        },
    )

    row = result.fetchone()
    db.commit()

    if row is None:
        return None

    return {
        "id": row.id,
        "title": row.title,
        "description": row.description,
        "user_id": row.user_id,
        "status": row.status,
    }


def get_tasks_filtered(
    db: Session,
    user_id: int | None = None,
    status: str | None = None,
):
    base_query = """
        SELECT id, title, description, user_id, status
        FROM tasks
    """

    conditions = []
    params = {}

    if user_id is not None:
        conditions.append("user_id = :user_id")
        params["user_id"] = user_id

    if status is not None:
        conditions.append("status = :status")
        params["status"] = status

    if conditions:
        base_query += " WHERE " + " AND ".join(conditions)

    base_query += " ORDER BY id"

    query = text(base_query)
    result = db.execute(query, params)
    rows = result.fetchall()

    return [
        {
            "id": row.id,
            "title": row.title,
            "description": row.description,
            "user_id": row.user_id,
            "status": row.status,
        }
        for row in rows
    ]