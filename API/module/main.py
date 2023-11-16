from pydantic import BaseModel, field_validator
from dto import ItemOrigin, InventoryItem
from typing import Dict, List
import json

from fastapi import FastAPI, HTTPException

app = FastAPI()

@app.get("/") #decorator function
async def root():
    return {"message":"hello world"}

# Expecting the serial num to be the keys of the dictionar
my_inventory_items: Dict[str, InventoryItem] = {}
my_inventory_item_dict: Dict[str, InventoryItem] = {}

item_origin = ItemOrigin(country="Ethiopia", production_date="10th Aug 2021")

# Create an in-memory list
my_inventory_items = [
  InventoryItem(name="printer", quantity=1, serial_number="H896", origin=item_origin)
]



@app.get("/items/{serial_number}")
def read_item(serial_number: str) -> InventoryItem:
    if serial_number in my_inventory_item_dict.keys():
        return my_inventory_item_dict[serial_number]
    else:
        raise HTTPException(status_code=404, detail=f"Could not find item with serial number {serial_number}")



    
    item = next((i for i in my_inventory_items if i.serial_number == serial_number), None)
    if item is None:
        raise HTTPException(status_code=404, detail=f"Could not find item with serial number {serial_number}")
    
    # Convert the item to a dictionary, ensuring nested models are properly converted
    item_dict = json.loads(json.dumps(item.dict()))
    return item_dict

@app.get("/items/")
def read_items() -> List[InventoryItem]:
    return my_inventory_item_dict.values()


'''
Requires something like:
{
    "name": "Product X",
    "quantity": 10,
    "serial_number": "H896",
    "origin": {
        "country": "Ethiopia",
        "production_date": "10th Aug 2000"
    }
}
in the body of the request.
'''
@app.put("/items/{serial_number}")
# item is passed by the request body as it is a complex type.
def update_item(serial_number:str, item:InventoryItem) -> None:
    my_inventory_item_dict[serial_number] = item
    print(serial_number)
    print(my_inventory_item_dict)

'''
    existing_item = next((i for i in my_inventory_items if i.serial_number == serial_number), None)
    #existing_item = my_inventory_items.get(serial_number)
    if existing_item:
        my_inventory_items.remove(existing_item)
    my_inventory_items.append(item)
    return item
'''

@app.delete("/items/{serial_number}")
def delete_item(serial_number:str) -> Dict:
    if serial_number in my_inventory_item_dict.keys():
        my_inventory_item_dict.pop(serial_number)
        return {"message":f"Deleted item {serial_number}"}
    else:
        raise HTTPException(status_code=404, detail=f"Could not find item with serial number {serial_number}")



# Run:
# $ uvicorn main:app --reload


