from pydantic import BaseModel, field_validator
from books.BookItem import BookItem

#from dto.ItemOrigin import ItemOrigin

class BookStore(BaseModel):
    name:str
    bookShelf:list[BookItem]
