import requests
url = 'https://api.pokemonbattle.ru/v2'
tokken = 'b715c2bc9248536f2d9be3422d0e077c'
HEADER = {'Content-Type':'application/json','trainer_token':tokken}
body_pokemons= {
    "name": "Бульбазавр25",
    "photo_id": 1
}
name_pokemon ={
    "pokemon_id": "195035",
    "name": "Zula2"
}
pokebol ={
    "pokemon_id": "195035"
}

"""response_create = requests.post(url= f'{url}/pokemons',headers = HEADER, json=body_pokemons)
print(response_create.text)"""


"""response_create = requests.patch(url= f'{url}/pokemons',headers = HEADER, json=name_pokemon)
print(response_create.text)"""

response_create = requests.post(url= f'{url}/trainers/add_pokeball',headers = HEADER, json=pokebol)
print(response_create.text)











