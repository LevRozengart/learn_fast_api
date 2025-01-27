import json
from fastapi import FastAPI, Query, HTTPException
from typing import Annotated
from pydantic import BaseModel, Field
from enum import Enum


app = FastAPI()
path = "users.json"

@app.get("/")
def home_page():
    return {"status": "ok"}

class Male(str, Enum):
    MALE = "male"
    FEMALE = "female"

class User(BaseModel):
    username: str = Field(..., min_length=4, max_length=15)
    password: str = Field(..., min_length=8, max_length=30)
    male: Male = None
@app.post("/auth/sign-up")
def sign_up(usermodel: User):
    username, password = usermodel.username, usermodel.password
    user_data = {"username": username, "password": password}
    if usermodel.male:
        user_data.update({"male": usermodel.male})
    try:
        with open(path) as f:
            lst_of_users = json.load(f)
            lst_of_users.append(user_data)
        for user in lst_of_users:
            if user["username"] == username:
                raise HTTPException(status_code=401, detail="уже есть человек с таким именем")
        with open(path, "w") as f:
            json.dump(lst_of_users, f, indent=2)
        return {"status": "ok"}
    except HTTPException as e:
        if e.status_code == 401:
            return {"status": "error", "desciption": e.detail}