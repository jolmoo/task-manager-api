from sqlalchemy import text
from sqlalchemy.orm import Session


def create_user(db: Session, name: str, email: str):
    query = text("""
        INSERT INTO users (name, email)
        VALUES (:name, :email)
        RETURNING id,name,email
    """)
    result = db.execute(query, {"name": name, "email": email})
    db.commit()

    row = result.fetchone()

    return{
        "id": row.id,
        "name": row.name,
        "email": row.email
    }

def get_users(db: Session):
    query = text("""
        SELECT * 
        FROM users
        ORDER BY id;
    """)
    result = db.execute(query)
    rows = result.fetchall()

    return [
        {
            "id": row.id,
            "name": row.name,
            "email": row.email,
        }
        for row in rows
    ]

def get_user_by_id(db: Session, user_id: int):
    query = text("""
        SELECT *
        FROM users
        WHERE id = :user_id      
    """)
    result = db.execute(query, {"user_id": user_id})
    row= result.fetchone()

    if row is None:
        return None
    
    return {
            "id": row.id,
            "name": row.name,
            "email": row.email,
        }
    
def get_user_by_email(db: Session, email: str):
    query = text("""
        SELECT *
        FROM users
        WHERE email = :email      
    """)   

    result = db.execute(query, {"email":email})
    row = result.fetchone()

    if row is None:
        return None
    return{
        "id": row.id,
        "name": row.name,
        "email": row.email,
    }

def update_user(db: Session, user_id: int, name: str, email: str):
    query = text("""
        UPDATE users
        SET name = :name,
            email = :email
        WHERE id = :user_id
        RETURNING id, name, email
    """)

    result = db.execute(
        query,
        {
            "user_id": user_id,
            "name": name,
            "email": email,
        },
    )
    db.commit()

    row = result.fetchone()

    if row is None:
        return None

    return {
        "id": row.id,
        "name": row.name,
        "email": row.email,
    }

def delete_user(db: Session, user_id: int):
    query = text("""
        DELETE FROM users
        WHERE id = :user_id
        RETURNING id          
    """)

    result = db.execute(query, {"user_id": user_id})
    db.commit()

    row = result.fetchone()

    if row is None:
        return None
    return row.id