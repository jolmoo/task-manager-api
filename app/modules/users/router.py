from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.core.db import get_db
from app.modules.users.schemas import UserCreate, UserResponse, UserUpdate
from app.modules.users.service import(
    create_user_service,
    get_user_by_id_service,
    get_users_service,
    update_user_service,
    delete_user_service
)

router = APIRouter(prefix="/users", tags=["users"])


@router.post("/", response_model=UserResponse)
def create_user_endpoint(payload: UserCreate, db:Session = Depends(get_db)):
    return create_user_service(db=db, name=payload.name, email=payload.email)

@router.get("/", response_model=list[UserResponse])
def get_users_endpoint(db: Session = Depends(get_db)):
    users = get_users_service(db=db)
    return users

@router.get("/{user_id}", response_model=UserResponse)
def get_users_by_id_endpoint(user_id: int,db:Session = Depends(get_db)):
    return get_user_by_id_service(db=db, user_id=user_id)

@router.put("/{user_id}", response_model=UserResponse)
def update_user_endpoint(
    user_id: int,
    payload: UserUpdate,
    db: Session = Depends(get_db),
):
    return update_user_service(
        db=db,
        user_id=user_id,
        name=payload.name,
        email=payload.email,
    )

@router.delete("/{user_id}")
def delete_user_endpoint(
    user_id: int,
    db: Session = Depends(get_db)
):
    return delete_user_service(db=db,user_id=user_id)