from fastapi import FastAPI

from app.modules.users.router import router as users_router
from app.modules.tasks.router import router as tasks_router

app = FastAPI(title="task-manager-api")

@app.get("/")
def root():
    return{
        "message":"API ready"
    }

app.include_router(users_router)
app.include_router(tasks_router)
