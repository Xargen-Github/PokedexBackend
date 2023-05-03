#!/usr/bin/env python
import sys
import json
from sql_app import database
from sql_app import crud
from schemas.pokemon_details import PokemonDetails
import requests

def to_pokemon_details(pokemon_data):
    pokemon_data["species"] = pokemon_data["species"]["name"]
    for stat in pokemon_data["stats"]:
        stat["stat"] =  stat["stat"]["name"]
    for ability in pokemon_data["abilities"]:
        ability["ability"] =  ability["ability"]["name"]
        
    forms = pokemon_data["forms"]
    if len(forms) > 0:
        pokemon_data["form"] = forms[0]["name"]
    return PokemonDetails(**pokemon_data)

def import_data(data):
    db = database.SessionLocal()
    print(data[0]["forms"])
    for pokemon_data in data:
        pd = to_pokemon_details(pokemon_data=pokemon_data)
        print(crud.add_pokemon(db, pd))
            
    db.close()


if len(sys.argv) > 1:
    match sys.argv[1]:
        case 'file':
            for arg in sys.argv[2:]:
                f = open(arg)
                data = json.load(f)
                f.close()
                import_data(data=data)
        case 'external':
            limit = 150
            data = []
            if len(sys.argv) > 2:
                limit = int(sys.argv[2])
            for i in range(1, limit):
                res = requests.get(f"https://pokeapi.co/api/v2/pokemon/{i}")
                pokemon = res.json()
                data.append(pokemon)
            print(data)
            import_data(data=data)
        case _:
            print("Use 'file' or 'external'")
else:
    print("Use 'file' or 'external'")
    
        