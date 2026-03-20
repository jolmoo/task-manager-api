from sqlalchemy.orm import Session
from fastapi import HTTPException

from app.modules.users.repository import (
    create_user,
    get_user_by_id,
    get_user_by_email,
    get_users,
    update_user,
    delete_user
)


def create_user_service(db: Session, name: str, email: str):
    existing_user = get_user_by_email(db=db, email=email)

    if existing_user:
        raise HTTPException(status_code=400, detail="Email already exists")

    return create_user(db=db, name=name, email=email)

def get_users_service(db: Session):
    return get_users(db=db)

def get_user_by_id_service(db: Session, user_id: int):
    user = get_user_by_id(db=db, user_id=user_id)

    if user is None:
        raise HTTPException(status_code=404, detail="User not found")

    return user


def update_user_service(db: Session, user_id: int, name: str, email: str):
    existing_user = get_user_by_id(db=db, user_id=user_id)

    if existing_user is None:
        raise HTTPException(status_code=404, detail="User not found")

    user_with_same_email = get_user_by_email(db=db, email=email)

    if user_with_same_email and user_with_same_email["id"] != user_id:
        raise HTTPException(status_code=400, detail="Email already exists")

    updated_user = update_user(db=db, user_id=user_id, name=name, email=email)

    return updated_user  

def delete_user_service(db: Session, user_id: int):
    delete_user_id = delete_user(db=db, user_id=user_id)

    if delete_user_id is None:
        raise HTTPException(status_code=404, detail= "User not found")
    
    return {"message": "User deleted successfully"}



