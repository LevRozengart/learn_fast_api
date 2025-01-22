from fastapi import FastAPI
from enum import Enum


app = FastAPI()

@app.get("/")
def home_page():
    return {"message: Hello!"}
