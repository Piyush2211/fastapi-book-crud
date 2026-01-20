from pydantic import BaseModel

class Book(BaseModel):#basically yeh class interface keh tarah kaam karti hai taki har ek attribute ke  type define ho sake
        id: int
        title: str
        author: str
        publisher: str
        published_date: str
        page_count: int
        language: str

class BookUpdate(BaseModel):
        title: str
        author: str
        publisher: str
        page_count: int
        language: str
