from lib2to3.pytree import Base
from typing import List, Optional
from pydantic import BaseModel

from models.page import Page 

class Chapter(BaseModel):
    id: str 
    title: str 
    images: Optional[List[str]]