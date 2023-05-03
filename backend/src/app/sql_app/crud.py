from sqlalchemy.orm import Session

from .models.user import User
from schemas.user import UserCreate
from .models.pokemon import Pokemon
from schemas.pokemon_details import PokemonDetails
from schemas.sort_enum import SortEnum

def get_all_pokemon(db: Session, sort: SortEnum = SortEnum.NAME_ASC):
    match sort:
        case SortEnum.NAME_ASC:
            sorter = Pokemon.name.asc()
        case SortEnum.NAME_DESC:
            sorter = Pokemon.name.desc()
        case SortEnum.ID_ASC:
            sorter = Pokemon.id.asc()
        case SortEnum.ID_DESC:
            sorter = Pokemon.id.asc()
        case _:
            sorter = Pokemon.name.asc()
            
    return db.query(Pokemon).order_by(sorter)

def get_pokemon_by_id(db: Session, id: int):
    return db.query(Pokemon).filter(Pokemon.id == id).first()

def add_pokemon(db: Session, pokemon: PokemonDetails):
    print(pokemon.name)
    db_pokemon = db.query(Pokemon).filter(Pokemon.id == pokemon.id).first()
    if db_pokemon:
        for key, value in pokemon.dict().items():
            if hasattr(db_pokemon, key):
                setattr(db_pokemon, key, value)
    else:
        db_pokemon = Pokemon(**pokemon.dict())
    db.add(db_pokemon)
    db.commit()
    db.refresh(db_pokemon)
    return db_pokemon

def get_user_by_email(db: Session, email: str):
    return db.query(User).filter(User.email == email).first()

def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(User).offset(skip).limit(limit).all()

def create_user(db: Session, user: UserCreate):
    fake_hashed_password = user.password + "notreallyhashed"
    db_user = User(email=user.email, name=user.name, password=fake_hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user