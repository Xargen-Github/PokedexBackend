from fastapi import FastAPI, Depends, HTTPException, status
from schemas.pokemon import Pokemon
from sqlalchemy.orm import Session
from sql_app.database import SessionLocal
import schemas
from schemas.sort_enum import SortEnum

from sql_app import crud

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
async def v1pokemons(db: Session = Depends(get_db), sort: SortEnum = SortEnum.NAME_ASC):
    return crud.get_all_pokemon(db=db, sort=sort)

@app.get("/api/v1/pokemons/{id}")
async def v1pokemons(id, db: Session = Depends(get_db)):
    db_pokemon = crud.get_pokemon_by_id(db=db, id=id)
    if not db_pokemon:
        raise HTTPException(status_code=404, detail="Pokemon not found")
    return db_pokemon

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

@app.get("/api/v1/teams/")
def v1_read_teams(db: Session = Depends(get_db)):
    return crud.get_teams(db)

@app.post("/api/v1/teams/", status_code=status.HTTP_201_CREATED)
def v1_create_team(team: schemas.team.TeamCreate, db: Session = Depends(get_db)):
    return crud.create_team(db=db, team=team)


@app.get("/api/v1/teams/{id}")
def v1_read_team(id: int, db: Session = Depends(get_db)):
    db_team = crud.get_team_by_id(db=db, id=id)
    if not db_team:
        raise HTTPException(status_code=404, detail="Team not found")
    return db_team

@app.post("/api/v1/teams/{id}")
def v1_update_team(id: int, team: schemas.team.TeamUpdate, db: Session = Depends(get_db)):
    if len(team.pokemon) > 6:
        raise HTTPException(status_code=400, detail="There is a maximum of 6 Pokémon per team")
    db_pokemon = crud.get_pokemon_by_ids(db=db, ids=team.pokemon)
    db_team = crud.get_team_by_id(db=db, id=id)
    if not db_team:
        raise HTTPException(status_code=404, detail="Team not found")
    return crud.update_team(db=db, db_team=db_team, db_pokemon=db_pokemon)