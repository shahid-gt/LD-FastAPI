from .database import Base, SessionLocal
from sqlalchemy import Column, Integer, String, Boolean


class Blog(Base):
    __tablename__ = 'blogs'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    published = Column(Boolean)
