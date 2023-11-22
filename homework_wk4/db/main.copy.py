# db/main.py

from typing import Optional
from sqlmodel import Field, Session, SQLModel, create_engine, select
from fastapi import FastAPI, HTTPException

# Create "Hero" DAO with primary key id and indexes on name and age fields.
class Hero(SQLModel, Table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str = Field(index=True)
    secret_name: str
    age: Optional[int] = Field(default=None, index=True)
    
# init sqlite
sqlite_filename = "database.db"
sqlite_url = f"sqlite:///{sqlite_filename}"

connect_args = {"check_same_thread":False}

hero_1 = Hero(name="Deadpond", secret_name="Dive Wilson")
hero_2 = Hero(name="Spider body", secret_name="Pedro")



engine = create_engine(sqlite_url, echo=True, connect_args=connect_args)
SQLModel.metadata.create_all(engine)


def create_db_and_tables():
    SQLModel.metadata.create_all(engine)
    print("Created db and tables")
    
app = FastAPI()


@app.on_event("startup")
def on_start_up():
    create_db_and_tables()

@app.post("/heroes/{name}")
def create_hero(hero:Hero):
    # implement part 1 here
    print(f"Created hero")
    pass

#app.get("/hero/name")
def get_hero(name:str):
    # implement part 2 here
    print("Created hero")
    pass

#app.get("/heroes/")
def get_heroes():
    # implement part 3 here
    pass


# Run:
# $ uvicorn main:app --reload
    
    
