from utilities import json_to_ld, ld_to_json, append_user
from fastapi import FastAPI


app = FastAPI()


@app.get("/")
def home_page():
    return {"message": "Hello!"}
@app.get("/sign-in/")
def authorization(username: str, password: str):
    users = json_to_ld("users.json")
    for user in users:
        if user["username"] == username:
            if user["password"] == password:
                return {"success": True}
            else:
                return {"success": False, "reason": "incorrect password"}
        return {"success": False, "reason": "username is not found"}


@app.get("/sign-up/")
def registraton(username: str, password: str):
    users = json_to_ld("users.json")
    a = append_user(users, username, password)
    if a:
        ld_to_json(a, "users.json")
        return {"success": True}
    else:
        return a