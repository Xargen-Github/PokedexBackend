#!/usr/bin/env python
import sys
import json
from sql_app import database
from sql_app import crud
from schemas.pokemon_details import PokemonDetails

for arg in sys.argv[1:]:
    f = open(arg)
    data = json.load(f)
    f.close()
    db = database.SessionLocal()
    print(data[0]["forms"])
    for pokemon_data in data:
        pokemon_data["species"] = pokemon_data["species"]["name"]
        for stat in pokemon_data["stats"]:
            stat["stat"] =  stat["stat"]["name"]
        for ability in pokemon_data["abilities"]:
            ability["ability"] =  ability["ability"]["name"]
            
        forms = pokemon_data["forms"]
        if len(forms) > 0:
            pokemon_data["form"] = forms[0]["name"]
            
        pd = PokemonDetails(**pokemon_data)
        print(crud.add_pokemon(db, pd))
            
    db.close()