import requests
import pytest

url = 'https://api.pokemonbattle.ru/v2'
TOKEN = 'b715c2bc9248536f2d9be3422d0e077c'
HEADER = {'Content-Type':'application/json','trainer_token':TOKEN}
TRAINER_ID = '13886'

def test_status_code():
    response = requests.get(url= f'{url}/trainers/', params = {'trainer_id': TRAINER_ID})
    assert response.status_code == 200

def test_part_of_response():
    response_get = requests.get(url= f'{url}/trainers/', params = {'trainer_id': TRAINER_ID})  
    assert response_get.json()["data"][0]["trainer_name"] == 'MrPyrlik'



    