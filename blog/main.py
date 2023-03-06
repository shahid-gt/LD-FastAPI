from fastapi import FastAPI
from models.blog import Blog
from static import blogs

app = FastAPI()


@app.post('/blog')
def create_blog(request: Blog):
    blogs.BLOGS.append(request)
    return blogs.BLOGS
