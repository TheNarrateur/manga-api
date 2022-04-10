from pydantic import BaseModel

class Page(BaseModel):
    number: int 
    image_url: str