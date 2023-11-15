from pydantic import BaseModel, field_validator, ValidationError, validator


class ItemOrigin(BaseModel):
    country:str
    production_date: str
    @field_validator("country")
    def check_valid_country(cls, country):
        assert country =="Ethiopia", f"Country {country} does not exist"    
        return country
