# pip3 install sqlmodel
# DAO
from typing import Optional
from sqlmodel import Field, SQLModel, Session, create_engine, select
from fastapi import FastAPI, HTTPException

# DAO class -> represents entry in the databasel.
class Hero(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True) # required
    name: str = Field(index=True)
    secret_name: str
    age: Optional[int] = None
    # team_id: Optional[int] = Field(default=None, foreign_key="team_id")

#hero_1 = Hero(name="Deadpond", secret_name="Dive Wilson")
#hero_2 = Hero(name="Spider body", secret_name="Pedro")

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

@app.get("/hero/{name}")
def get_hero(name:str):
    with Session(engine) as session:
        statement = select(Hero).where(Hero.name == name)
        hero = session.exec(statement).first()
        return hero

@app.get("/heroes/")
def get_heroes():
    with Session(engine) as session:
        statement = select(Hero)
        heroes = session.exec(statement).all()
        return heroes


# Run:
# $ uvicorn main:app --reload