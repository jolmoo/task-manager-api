from fastapi import HTTPException
from sqlalchemy.orm import Session

from app.modules.users.repository import get_user_by_id
from app.modules.tasks.repository import (
    create_task,
    get_tasks_by_user_id,
    get_task_by_id,
    get_all_tasks,
    delete_task_by_id,
    update_task_by_id,
    update_task_status,
    get_tasks_filtered,
)


def create_task_service(
    db: Session,
    title: str,
    description: str | None,
    user_id: int,
):
    user = get_user_by_id(db=db, user_id=user_id)

    if user is None:
        raise HTTPException(status_code=404, detail="User not found")

    return create_task(db=db, title=title, description=description, user_id=user_id)


def get_tasks_by_user_id_service(db: Session, user_id: int):
    user = get_user_by_id(db=db, user_id=user_id)

    if user is None:
        raise HTTPException(status_code=404, detail="User not found")

    return get_tasks_by_user_id(db=db, user_id=user_id)


def get_task_by_id_service(db: Session, task_id: int):
    result = get_task_by_id(db=db, task_id=task_id)

    if result is None:
        raise HTTPException(status_code=404, detail="Task not found")

    return result


def get_all_tasks_service(db: Session):
    return get_all_tasks(db=db)


def delete_task_by_id_service(db: Session, task_id: int):
    deleted_task_id = delete_task_by_id(db=db, task_id=task_id)

    if deleted_task_id is None:
        raise HTTPException(status_code=404, detail="Task not found")

    return {"message": "Task deleted successfully"}


def update_task_by_id_service(
    db: Session,
    task_id: int,
    title: str,
    description: str | None,
    user_id: int,
):
    existing_task = get_task_by_id(db=db, task_id=task_id)

    if existing_task is None:
        raise HTTPException(status_code=404, detail="Task not found")

    user = get_user_by_id(db=db, user_id=user_id)

    if user is None:
        raise HTTPException(status_code=404, detail="User not found")

    return update_task_by_id(
        db=db,
        task_id=task_id,
        title=title,
        description=description,
        user_id=user_id,
    )


def update_task_status_service(db: Session, task_id: int, status: str):
    allowed_statuses = ["pending", "in_progress", "done"]

    task = get_task_by_id(db=db, task_id=task_id)

    if task is None:
        raise HTTPException(status_code=404, detail="Task not found")

    if status not in allowed_statuses:
        raise HTTPException(
            status_code=400,
            detail=f"Invalid status. Allowed values: {allowed_statuses}",
        )

    return update_task_status(db=db, task_id=task_id, status=status)


def get_tasks_filtered_service(
    db: Session,
    user_id: int | None = None,
    status: str | None = None,
):
    allowed_statuses = ["pending", "in_progress", "done"]

    if status is not None and status not in allowed_statuses:
        raise HTTPException(
            status_code=400,
            detail=f"Invalid status. Allowed values: {allowed_statuses}",
        )

    return get_tasks_filtered(db=db, user_id=user_id, status=status)