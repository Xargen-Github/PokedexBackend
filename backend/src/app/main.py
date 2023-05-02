from fastapi import FastAPI, Depends, HTTPException
from schemas.pokemon import Pokemon
from sqlalchemy.orm import Session
from sql_app.database import Base, engine, SessionLocal
import schemas

from sql_app import crud

Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/api/v1/pokemons")
async def v1pokemons(db: Session = Depends(get_db)):
    return crud.get_all_pokemon(db=db)

@app.get("/api/v1/pokemons/{id}")
async def v1pokemons(id, db: Session = Depends(get_db)):
    return crud.get_pokemon_by_id(db=db, id=id)

@app.post("/users/", response_model=schemas.user.User)
def create_user(user: schemas.user.UserCreate, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return crud.create_user(db=db, user=user)

@app.get("/users/", response_model=list[schemas.user.User])
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = crud.get_users(db, skip=skip, limit=limit)
    return users