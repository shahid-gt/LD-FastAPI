from fastapi import FastAPI, Depends, status, Response, HTTPException
# from .dependencies import get_query_token, get_token_number
from typing import List
from static import blogs
from . import models, schemas
from .database import engine, SessionLocal
from sqlalchemy.orm import Session
from .database import get_db
from .routers import blog
models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(blog.router)
# def get_db():
#     db = SessionLocal()
#     try:
#         yield db
#     finally:
#         db.close()


@app.post('/blog', status_code=status.HTTP_201_CREATED)
def create_blog(request: schemas.Blog, db: Session = Depends(get_db)):
    new_blog = models.Blog(name=request.name, published=request.published)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog


# @app.get('/blogs', response_model=List[schemas.Blog])
# def get_blog(db: Session = Depends(get_db)):
#     blogs = db.query(models.Blog).all()
#     return blogs


@app.get('/blog/{id}', status_code=status.HTTP_200_OK, response_model=schemas.Blog)
def show(id, response: Response, db: Session = Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"{'details': f'blog with {id} is not found.'}")
        # response.status_code = status.HTTP_404_NOT_FOUND
        # return {'details': f'blog with {id} is not found.'}
    return blog


@app.put('/blog/{id}', status_code=status.HTTP_202_ACCEPTED)
def update(id, request: schemas.Blog, db: Session = Depends(get_db)):
    blog = db.query(models.Blog).filter(
        models.Blog.id == id)
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'blog with {id} is not found.')
    blog.update(request.dict())
    db.commit()
    return f'blog with {id} is updated successfully.'
