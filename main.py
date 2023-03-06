from fastapi import FastAPI
from typing import Union
from models.blog import Blog
from static import blogs

app = FastAPI()


@app.get('/')
def index():
    return {'message': 'HEY! this is just start'}


@app.get('/blogs/filter')
def filter_blogs(published: bool | None = None):
    result = []
    if published is None:
        return blogs.BLOGS

    for blog in blogs.BLOGS:
        if blog["published"] == published:
            result.append(blog)
    return result


@app.get('/items/{item_id}')
def read_item(item_id: int, q: Union[str, None] = None):
    return {'item_id': item_id, "q": q}


@app.post('/blog')
def create_blog(request: Blog):
    blogs.BLOGS.append(request)
    return blogs.BLOGS
