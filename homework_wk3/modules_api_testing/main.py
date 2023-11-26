#from pydantic import BaseModel, field_validator
from pydantic import BaseModel
from dto import ItemOrigin, InventoryItem
from typing import Dict, List
import json
from functools import reduce

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
'''
my_inventory_items = [
  InventoryItem(name="printer", quantity=1, serial_number="H896", origin=item_origin)
]

'''


# OK
@app.get("/items/{serial_number}")
def read_item(serial_number: str): # -> InventoryItem
    #return my_inventory_item_dict
    #yield my_inventory_item_dict
    # Convert in memory item list to dictionary indexed by serial keys
    d = reduce(lambda acc, item:{**acc, **item}, my_inventory_item_dict, {})
    return {}
    if my_inventory_item_dict[serial_number]:
        return my_inventory_item_dict[serial_number]
    else:
        raise HTTPException(status_code=404, detail=f"Could not find item with serial number {serial_number}")


@app.get("/items/")
def read_items():
    # Returns a list object where each item is a dictionary object with serial number as key.
    return my_inventory_item_dict

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
    #yield(serial_number) # [<serial _number>]
    '''
    [
        {
            "name": "Product X",
            "quantity": 1,
            "serial_number": "",
            "origin": {
                "country": "Ethiopia",
                "production_date": "11 Oct 2300"
            }
        },
        {
           ... 
            
        }
    ]
    '''
    yield(my_inventory_item_dict.items())

'''
    existing_item = next((i for i in my_inventory_items if i.serial_number == serial_number), None)
    #APIexisting_item = my_inventory_items.get(serial_number)
    if existing_item:
        my_inventory_items.remove(existing_item)
    my_inventory_items.append(item)
    return item
'''


'''
@app.get("/items/")
def read_items() -> List[InventoryItem]:
    return {}
    #return my_inventory_item_dict.values()

'''



@app.delete("/items/{serial_number}")
def delete_item(serial_number:str) -> Dict:
    if serial_number in my_inventory_item_dict.keys():
        my_inventory_item_dict.pop(serial_number)
        if serial_number in my_inventory_item_dict.keys():
            raise HTTPException(status_code=300, detail=f"Failed to delete with serial number {serial_number}")
        return {"message":f"Deleted item {serial_number}"}
    else:
        raise HTTPException(status_code=404, detail=f"Could not find item with serial number {serial_number}")



# Run:
# $ uvicorn main:app --reload --port 8001


