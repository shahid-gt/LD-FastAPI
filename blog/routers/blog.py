from fastapi import APIRouter, Depends
from typing import List
from ..database import get_db
from .. import schemas, models
from sqlalchemy.orm import Session

router = APIRouter()


@router.get('/blogs', response_model=List[schemas.Blog], tags=["blogs"])
def get_blog(db: Session = Depends(get_db)):
    blogs = db.query(models.Blog).all()
    return blogs
