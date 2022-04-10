from typing import List, Optional
from pydantic import BaseModel

from models.chapter import Chapter

class Manga(BaseModel):
    id: str 
    title: str 
    image: str 
    description: Optional[str]
    chapters: Optional[List[Chapter]]