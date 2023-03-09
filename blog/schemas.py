from pydantic import BaseModel
from typing import Optional


class Blog(BaseModel):
    name: str
    published: Optional[bool]

    class Config():
        orm_mode = True
