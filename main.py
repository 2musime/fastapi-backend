from fastapi import FastAPI
from fastapi.params import Body
from pydantic import BaseModel
from typing import Optional

class Post(BaseModel):
    id: int
    title: str
    content: str
    published: bool = True
    rating:Optional[int] = None

app = FastAPI()

posts = [
    {"id": 1, "title": "First Post", "content": "Hello world", "published": True, "rating": 5},
    {"id": 2, "title": "Second Post", "content": "Learning FastAPI", "published": True, "rating": 4},
]

@app.get("/")
def root():
    return {"message": "Hello, David!"}

@app.get("/posts")
def get_posts():
    return {"posts":posts}

@app.post("/posts")
def create_post(new_post: Post):
    print(new_post)
    return {"new_post": f"title: {new_post.title}, content: {new_post.content}"}

@app.get("/posts/{id}")
def get_post(id: int):
    for post in posts:
        if post["id"] == id:
            return {"post": post}
    return {"message": "no post found"}