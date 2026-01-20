from fastapi import FastAPI ,status
from fastapi.exceptions import HTTPException
from pydantic import BaseModel
from typing import List
app = FastAPI()





books = [
    {
        "id": 1,
        "title": "Think Python",
        "author": "Allen B. Downey",
        "publisher": "O'Reilly Media",
        "published_date": "2015-08-01",
        "page_count": 300,
        "language": "English",
    },
    {
        "id": 2,
        "title": "Python Crash Course",
        "author": "Eric Matthes",
        "publisher": "No Starch Press",
        "published_date": "2019-05-03",
        "page_count": 544,
        "language": "English",
    },
    {
        "id": 3,
        "title": "Fluent Python",
        "author": "Luciano Ramalho",
        "publisher": "O'Reilly Media",
        "published_date": "2022-04-19",
        "page_count": 1014,
        "language": "English",
    },
    {
        "id": 4,
        "title": "Automate the Boring Stuff with Python",
        "author": "Al Sweigart",
        "publisher": "No Starch Press",
        "published_date": "2020-11-12",
        "page_count": 592,
        "language": "English",
    },
    {
        "id": 5,
        "title": "Clean Code",
        "author": "Robert C. Martin",
        "publisher": "Prentice Hall",
        "published_date": "2008-08-01",
        "page_count": 464,
        "language": "English",
        
    }
]
#basically yaha apna database banake joh keh array of dictionary hai hamne crud operations perform kare hai using fastapi 
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

@app.get("/books",response_model=List[Book])#idhar hamne list of book  joh keh ek class hai BaseModal use karke create kair huyi usme saari books koh return kara hai
async def get_all_books():
    return books

@app.post("/books",status_code =status.HTTP_201_CREATED)
async def create_book(book_data:Book)->dict:
    new_book = book_data.model_dump()
    books.append(new_book)
    return new_book


@app.get("/book/{book_id}")
async def get_book(book_id:int)->dict:
    for book in books:
        if book['id']==book_id:
            return book
    
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Book not found") 


@app.patch("/book/{book_id}")
async def update_book(book_id:int,book_update_data:BookUpdate)->dict:
    for book in books:
         if book['id'] == book_id:
              book['title']=book_update_data.title
              book['publisher']=book_update_data.publisher
              book['page_count']= book_update_data.page_count
              book['language']=book_update_data.language    
              return book
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Book not found")
@app.delete("/book/{book_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_book(book_id: int):
    for book in books:
        if book["id"] == book_id:
            books.remove(book)
            return  # ✅ no body for 204

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Book not found"
    )
