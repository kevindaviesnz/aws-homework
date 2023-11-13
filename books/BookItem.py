from pydantic import BaseModel, field_validator
from books.Author import Author

class BookItem(BaseModel):
    name: str
    author: Author
    year_published:int
    @field_validator("year_published")
    @classmethod
    def check_valid_year_published(cls, year_published:int):
        assert year_published not in range(2010, 2023), f"Year published is not valid"