from fastapi import FastAPI
from static import blogs
from .schemas import Blog
from . import models
from .database import engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


@app.post('/blog')
def create_blog(request: Blog):
    blogs.Blog.append(request)
    return blogs
