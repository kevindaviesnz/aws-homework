# Note: Newer versions of pydantic use validator instead of field_validator
from pydantic import BaseModel, validator
from .ItemOrigin import ItemOrigin

# Data transfer object
class InventoryItem(BaseModel):
    name:str
    quantity: int
    serial_number:str
    origin: ItemOrigin
