from fastapi import FastAPI
from enum import Enum


app = FastAPI()

@app.get("/")
def home_page():
    return {"message": "Hello!"}


class Classmates(str, Enum):
    classmate_1 = "Gleb"
    classmate_2 = "Kostya"

@app.get("/dodiki/{name}")
async def get_eblans(name: Classmates):
    if name.value == "Gleb":
        return {"returned_eblan": name}
    return {"returned_eblan": name}


items = {
    1: "ball",
    2: "shoes"
}

item_in_stock = {
    1: True,
    2: False
}

@app.get("/item/{item_id}/status")
async def read_item(item_id: int, in_stock: bool | None = None):
    item = {"item": items[item_id]}
    if in_stock:
        item.update({"in_stock": item_in_stock[item_id]})
    return item