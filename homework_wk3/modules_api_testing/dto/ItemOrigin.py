# Note: Newer versions of pydantic use validator instead of field_validator
from pydantic import BaseModel, ValidationError, validator


class ItemOrigin(BaseModel):
    country:str
    production_date: str
    @validator("country")
    def check_valid_country(cls, country):
        assert country =="Ethiopia", f"Country {country} does not exist"    
        return country
