from fastapi import FastAPI, Query
from typing import Annotated
from pydantic import BaseModel, Field
import json
from json import JSONDecodeError


app = FastAPI()


class SAddMovie(BaseModel):
    title: str
    genre: str
    year: int

@app.post("/movies/")
def add_movie(moviemodel: SAddMovie):
    try:
        with open("movies.json") as f:
            lst_of_movies = json.load(f)
    except (JSONDecodeError, FileNotFoundError):
        with open("movies.json", "w") as f:
            lst_of_movies = list()
    max_id = max([i["id"] for i in lst_of_movies])
    moviemodel = dict(moviemodel)
    moviemodel.update({"id": max_id+1})
    lst_of_movies.append(moviemodel)
    try:
        with open("movies.json", "w") as f:
            json.dump(lst_of_movies, f, indent=2)
            return moviemodel
    except Exception as e:
        return {"error": str(e)}


@app.get("/movies/")
def get_movies(
        title: str | None = None,
        genre: str | None = None,
        year: int | None = None
):
    try:
        with open("movies.json") as f:
            lst_of_movies = json.load(f)
    except FileNotFoundError as e:
        return {"error": str(e)}

    if title:
        lst_of_movies = [i for i in lst_of_movies if i["title"] == title]
    if genre:
        lst_of_movies = [i for i in lst_of_movies if i["genre"] == genre]
    if year:
        lst_of_movies = [i for i in lst_of_movies if i["year"] == year]

    if lst_of_movies:
        return lst_of_movies
    else:
        return {"error": "not movies for your query"}

@app.get("/movies/{movie_id}")
def get_movie_by_id(movie_id: int):
    try:
        with open("movies.json") as f:
            lst_of_movies = json.load(f)
    except (JSONDecodeError, FileNotFoundError) as e:
        return {"error": str(e)}

    for movie in lst_of_movies:
        if movie["id"] == movie_id:
            return movie
    return {"error": "movie with this id is not found"}


@app.delete("/movies/{movie_id}")
def delete_movies_by_id(movie_id: int):
    try:
        with open("movies.json") as f:
            lst_of_movies = json.load(f)
    except Exception as e:
        return {"status": "error"}

    new_lst = []
    returned_status = {}
    for movie in lst_of_movies:
        if movie["id"] == movie_id:
            returned_status = {"message": f"Movie with ID {movie_id} had been deleted"}
        else:
            new_lst.append(movie)
    if not returned_status:
        returned_status = {"error": f"Not movie with {movie_id}"}
    with open("movies.json", "w") as f:
        json.dump(new_lst, f, indent=2)
    return returned_status
