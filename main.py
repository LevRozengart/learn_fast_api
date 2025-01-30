from fastapi import FastAPI
from pydantic import BaseModel


app = FastAPI()


class Task(BaseModel):
    name: str
    description: str | None


@app.get("/tasks")
def get_tasks():
    task = Task(name="Сделай дз по инфе")
    return {"data": task}