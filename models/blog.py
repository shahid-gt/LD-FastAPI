from pydantic import BaseModel
from typing import Optional

class Blog(BaseModel):
    id: str | int
    name: str
    published: Optional[bool]