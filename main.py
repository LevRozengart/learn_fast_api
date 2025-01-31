from fastapi import FastAPI
from pydantic import BaseModel
import json

app = FastAPI()


class SBook(BaseModel):
    title: str
    author: str
    year: int | None = None

@app.post("/books/")
def add_book(bookmodel: SBook):
    with open("book.json") as f:
        lst_of_books: list = json.load(f)
    lst_of_books.append({"id": len(lst_of_books) + 1,
                         "title": bookmodel.title,
                         "author": bookmodel.author,
                         "year": bookmodel.year})
    with open("book.json", "w") as f:
        json.dump(lst_of_books, f, indent=2)
    return {"id": len(lst_of_books),
            "title": bookmodel.title,
            "author": bookmodel.author,
            "year": bookmodel.year}


@app.get("/books/")
def get_lst_of_books():
    with open("book.json") as f:
        lst_of_books = json.load(f)
    return lst_of_books

@app.get("/books/{book_id}")
def get_by_id(book_id: int):
    with open("book.json") as f:
        lst_of_books = json.load(f)
    for book in lst_of_books:
        if book["id"] == book_id:
            return book
    return {"error": "book isn't found"}