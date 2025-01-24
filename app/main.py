from utilities import json_to_ld
from fastapi import FastAPI


app = FastAPI()


@app.get("/")
def home_page():
    return {"message": "Hello!"}
@app.get("/{username}/{password}")
def authorization(username: str, password: str):
    users = json_to_ld("users")
    for user in users:
        if user["username"] == username:
            if user["password"] == password:
                return {"success": True}
            else:
                return {"success": False, "reason": "incorrect password"}
        return {"success": False, "reason": "username is not found"}
