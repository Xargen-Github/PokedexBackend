from sqlalchemy.orm import Session

from .models.user import User
from schemas.user import UserCreate
from .models.pokemon import Pokemon
from .models.sprites import Sprites
from .models.type_slot import TypeSlot
from .models.move import Move
from .models.stat import Stat
from .models.ability import Ability
from .models.version_group_detail import VersionGroupDetail
from .models.type import Type
from schemas.pokemon_details import PokemonDetails
from schemas.sort_enum import SortEnum
from schemas.team import TeamCreate
from .models.team import Team

def get_all_pokemon(db: Session, sort: SortEnum = SortEnum.NAME_ASC):
    match sort:
        case SortEnum.NAME_ASC:
            sorter = (Pokemon.name.asc())
        case SortEnum.NAME_DESC:
            sorter = (Pokemon.name.desc())
        case SortEnum.ID_ASC:
            sorter = (Pokemon.id.asc())
        case SortEnum.ID_DESC:
            sorter = (Pokemon.id.desc())
        case _:
            sorter = (Pokemon.name.asc())
            
    return db.query(Pokemon).order_by(sorter).all()

def get_pokemon_by_id(db: Session, id: int):
    return db.query(Pokemon).filter(Pokemon.id == id).first()

def get_pokemon_by_ids(db: Session, ids: list[int]):
    return db.query(Pokemon).filter(Pokemon.id.in_(ids)).all()

def add_pokemon(db: Session, pokemon: PokemonDetails):
    print(pokemon.name)
    db_pokemon = db.query(Pokemon).filter(Pokemon.id == pokemon.id).first()
    if not db_pokemon:
        db_pokemon = Pokemon(id=pokemon.id, name=pokemon.name)
    
    if pokemon.sprites:
        db_sprites = db.query(Sprites).filter(Sprites.id == pokemon.sprites.id).first()
        if not db_sprites:
            db_sprites = Sprites(**pokemon.sprites.dict())
        else:
            update_model_with_schema(db_sprites, pokemon.sprites)
            
        db.add(db_sprites)
        db_pokemon.sprites = db_sprites
        
    if pokemon.types:
        db_type_slots = []
        for type_slot in pokemon.types:
            db_type = db.query(Type).filter(Type.name == type_slot.type.name).first()
            if not db_type:
                db_type = Type(**type_slot.type.dict())
            else:
                update_model_with_schema(db_type, type_slot.type)
            db.add(db_type)
            
            db_type_slot = db.query(TypeSlot).filter(TypeSlot.slot == type_slot.slot and TypeSlot.pokemon_id == pokemon.id).first()
            if not db_type_slot:
                db_type_slot = TypeSlot(pokemon_type=db_type, pokemon_type_id=db_type.id, pokemon_id=db_pokemon.id, pokemon=db_pokemon, slot=type_slot.slot)
            else:
                db_type_slot.pokemon_type = db_type
                db_type_slot.pokemon = db_pokemon
            db.add(db_type_slot)
            db_type_slots.append(db_type_slot)
        db_pokemon.types = db_type_slots
    
    db_pokemon.height = pokemon.height
    db_pokemon.weight = pokemon.weight
    
    if pokemon.moves:
        db_moves = []
        for move in pokemon.moves:
            db_move = db.query(Move).filter(Move.move == move.move and Move.pokemon_id == db_pokemon.id).first()
                
            db_version_group_details = []
            for version_group_detail in move.version_group_details:
                db_version_group_detail = None
                if db_move:
                    db_version_group_detail = db.query(VersionGroupDetail).filter(VersionGroupDetail.version_group == version_group_detail.version_group and VersionGroupDetail.move_id == db_move.id).first()
                if not db_version_group_detail:
                    db_version_group_detail = VersionGroupDetail(**version_group_detail.dict())
                else:
                    update_model_with_schema(db_version_group_detail, version_group_detail)
                db.add(db_version_group_detail)
                db_version_group_details.append(db_version_group_detail)
                
            move.version_group_details = db_version_group_details
            if not db_move:
                db_move = Move(**move.dict())
            else:
                update_model_with_schema(db_move, move)
                
            db.add(db_move)
            db_moves.append(db_move)
        db_pokemon.moves = db_moves
    
    db_pokemon.order = pokemon.order
    db_pokemon.species = pokemon.species
    
    if pokemon.stats:
        db_stats = []
        for stat in pokemon.stats:
            db_stat = db.query(Stat).filter(Stat.stat == stat.stat and Stat.pokemon_id == db_pokemon.id).first()
            if not db_stat:
                db_stat = Stat(**stat.dict())
            else:
                update_model_with_schema(db_stat, stat)
            db.add(db_stat)
            db_stats.append(db_stat)
        db_pokemon.stats = db_stats

    if pokemon.abilities:
        db_abilities = []
        for ability in pokemon.abilities:
            db_Ability = db.query(Ability).filter(Ability.slot == ability.slot and Ability.pokemon_id == db_pokemon.id).first()
            if not db_Ability:
                db_Ability = Ability(**ability.dict())
            else:
                update_model_with_schema(db_Ability, ability)
            db.add(db_Ability)
            db_abilities.append(db_Ability)
        db_pokemon.abilities = db_abilities
    
    db_pokemon.form = pokemon.form
    
    db.add(db_pokemon)
    db.commit()
    db.refresh(db_pokemon)
    return db_pokemon

def update_model_with_schema(model, schema):
    for key, value in schema.dict().items():
        if hasattr(model, key):
            setattr(model, key, value)

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

def get_teams(db: Session):
    return db.query(Team).order_by(Team.name.asc()).all();

def create_team(db: Session, team: TeamCreate):
    db_team = Team(**team.dict())
    db.add(db_team)
    db.commit()
    db.refresh(db_team)
    return db_team

def get_team_by_id(db: Session, id: int):
    return db.query(Team).filter(Team.id == id).first()

def update_team(db:Session, db_team: Team, db_pokemon: list[Pokemon]):
    db_team.pokemon = db_pokemon
    db.add(db_team)
    db.commit()
    db.refresh(db_team)
    return db_team