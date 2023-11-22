# pip3 install sqlmodel
# DAO
# http://localhost:8000/#docs
from typing import Optional, List
from sqlmodel import Field, SQLModel, Session, create_engine, select
from fastapi import FastAPI, HTTPException

# DAO class -> represents entry in the database.
class Hero(SQLModel, table=True): # DAO: table-True
    id: Optional[int] = Field(default=None, primary_key=True) # required
    name: str = Field(index=True)
    secret_name: str
    age: Optional[int] = None
    # team_id: Optional[int] = Field(default=None, foreign_key="team_id")

# init sqlite
sqlite_filename = "database.db"
sqlite_url = f"sqlite:///{sqlite_filename}"
connect_args = {"check_same_thread":False}
engine = create_engine(sqlite_url, echo=True, connect_args=connect_args)

def create_db_and_tables():
    SQLModel.metadata.create_all(engine)
    print("Created db and tables")
    
app = FastAPI()

@app.on_event("startup")
def on_start_up():
    create_db_and_tables()
 
@app.post("/heroes/{name}")
def create_hero(hero:Hero, name:str):
    hero.name = name    
    with Session(engine) as session:
        session.add(hero)
        session.commit()
    yield(f"Created hero {name}")

@app.get("/hero/{name}", response_model=Hero)
def get_hero(name:str):
    with Session(engine) as session:
        statement = select(Hero).where(Hero.name == name)
        hero = session.exec(statement).first()
        # Need to add exception handling if hero not found
        return hero

@app.get("/heroes/", response_model=List[Hero])
def get_heroes():
    with Session(engine) as session:
        statement = select(Hero)
        heroes = session.exec(statement).all()
        return heroes

# PATCH
# Define new DTO model specialise class only for doing updates (read, update, create)
# Defines what info is required.
class HeroUpdateDTO(SQLModel):
    name: Optional[str] = None
    secret_name: Optional[str] = None
    age: Optional[int] = None


'''
body  - raw  - json
{
    "name":"Deadpool",
    "secret_name": "Thor"
}
'''
@app.patch("/hero", response_model=Hero)
def change_secret_name(hero_update:HeroUpdateDTO):
    with Session(engine) as session:
        statement = session.select(Hero).where(Hero.name == HeroUpdateDTO.name)
        db_hero = session.exec(statement).first()
        # to do : exccepton handling
        hero_data = hero_update.dict(exclude_unset=True)
        for key, value in hero_data.items():
            setattr(db_hero, key, value)
        session.add(db_hero)
        session.commit()
        session.refresh(db_hero)







# Run:
# $ uvicorn main:app --reload