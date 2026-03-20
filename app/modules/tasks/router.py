from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.core.db import get_db
from app.modules.tasks.schemas import TaskCreate, TaskResponse, TaskUpdate
from app.modules.tasks.service import (
    create_task_service,
    get_task_by_id_service,
    delete_task_by_id_service,
    update_task_by_id_service,
    update_task_status_service,
    get_tasks_filtered_service,
)

router = APIRouter(prefix="/tasks", tags=["tasks"])


@router.post("/", response_model=TaskResponse)
def create_task_endpoint(payload: TaskCreate, db: Session = Depends(get_db)):
    return create_task_service(
        db=db,
        title=payload.title,
        description=payload.description,
        user_id=payload.user_id,
    )


@router.get("/", response_model=list[TaskResponse])
def get_tasks_endpoint(
    user_id: int | None = None,
    status: str | None = None,
    db: Session = Depends(get_db),
):
    return get_tasks_filtered_service(
        db=db,
        user_id=user_id,
        status=status,
    )


@router.get("/{task_id}", response_model=TaskResponse)
def get_task_by_id_endpoint(task_id: int, db: Session = Depends(get_db)):
    return get_task_by_id_service(db=db, task_id=task_id)


@router.delete("/{task_id}")
def delete_task_by_id_endpoint(task_id: int, db: Session = Depends(get_db)):
    return delete_task_by_id_service(db=db, task_id=task_id)


@router.put("/{task_id}", response_model=TaskResponse)
def update_task_endpoint(
    task_id: int,
    payload: TaskUpdate,
    db: Session = Depends(get_db),
):
    return update_task_by_id_service(
        db=db,
        task_id=task_id,
        title=payload.title,
        description=payload.description,
        user_id=payload.user_id,
    )


@router.patch("/{task_id}/status", response_model=TaskResponse)
def update_status_endpoint(
    task_id: int,
    status: str,
    db: Session = Depends(get_db),
):
    return update_task_status_service(
        db=db,
        task_id=task_id,
        status=status,
    )