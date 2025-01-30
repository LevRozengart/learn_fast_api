from fastapi import FastAPI, Depends
from pydantic import BaseModel
from typing import Annotated


app = FastAPI()


class STaskAdd(BaseModel):
    name: str
    description: str | None = None


class STask(STaskAdd):
    id: int

tasks = []

@app.post("/tasks")
async def add_task(
        task: Annotated[STaskAdd, Depends()]
):
    tasks.append(task)
    return {"ok": True}

# @app.get("/tasks")
# def get_tasks():
#     task = STask(name="Сделай дз по инфе")
#     return {"data": task}