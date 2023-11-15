from typing import Union

# pip3 install fastapi[all]
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# REST: GET, POST, PUT, DELETE, OPTION (what kind of API method is available).
# GRPC: small and efficient for data transfer.

'''
(Sync API)
Client ----> Server
Client <-- 201 --- Server
Client ----> Server
Client <-- 200 --- Server
'''

'''
Ways of providing input: path, query, header, body
'''
@app.get("/") #decorator function
async def root():
    return {"message":"hello world"}

class Item(BaseModel):
    name: str
    price:float


@app.get("/items/{item_id}")
# as q is not mentioned in the get request it becomes a query parameter
def read_item(item_id:int, item: Item):
    return {"item_id":item_id}


'''
@app.get("/items/{item_id}")
# as q is not mentioned in the get request it becomes a query parameter
def read_item(item_id:int, item: Item, item2: Item, q:Union[str, None]=None):
    return {"item_id":item_id, "q":q}
'''


#upgrades
# item is passed by the request body as it is a complex type.
@app.put("/items/{item_id}")
def update_item(item_id:int, item:Item):
    return {"item_id":item_id, "item": item}
    

# Run:
# $ uvicorn main:app --reload