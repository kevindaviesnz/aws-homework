from pydantic import BaseModel, field_validator
import re
#from dto.ItemOrigin import ItemOrigin

class Author(BaseModel):
    name: str
    author_id:str
    @field_validator("name")
    @classmethod
    def check_valid_author_name(cls, author_name:str):
        assert author_name.istitle() == False, f"Name {author_name} should be a title"
    @field_validator("author_id")
    @classmethod
    def check_valid_author_id(cls, author_id:str):
        pattern = re.compile(r'^[A-Z]{4}-\d{4}$')
        assert pattern.match(author_id), f"Author id {author_id} is not in the format XXXX-YYYY where X is a capital letter and Y is a number."
        

