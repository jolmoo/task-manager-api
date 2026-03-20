from pydantic import BaseModel, EmailStr

class TaskCreate(BaseModel):
    title: str
    description: str | None = None
    user_id: int

class TaskResponse(BaseModel):
    id: int
    title: str
    description: str | None = None
    user_id : int
    status: str 

class TaskUpdate(BaseModel):    
    title: str
    description: str | None = None
    user_id: int
    