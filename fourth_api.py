from fastapi import FastAPI, Depends
from pydantic import  BaseModel
from typing import Optional, Annotated
from contextlib import asynccontextmanager
from datebase import create_tables

@asynccontextmanager
async def lifespan(app: FastAPI):
    await  delete_tables()
    print("Clear")
    await  create_tables()
    print("Ready")
    yield
    print("End")


app = FastAPI(lifespan=lifespan)


class STaskAdd(BaseModel):
    name:str
    description: Optional[str] = None

class STask(BaseModel):
    id: int

tasks=[]

@app.post("/tasks")
async def add_task(
        task: Annotated[STaskAdd, Depends()],

):
    tasks.append(task)
    return{"ok": True}


# @app.get("/tasks")
# def get_tasks():
#     task=Task(name="aye")
#     return {"data": "Hello"}