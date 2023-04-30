import requests
import pytest

def  Add_a_new_password() :
    response = requests.get('https://pokemonbattle.me:9104/trainers' , headers={'trainer_token':'4b73c485e194de4704b4c76474ae9052'})
    assert response.status_code == 200

    
def Add_a_trainer() :
    response1 = requests.get('https://pokemonbattle.me:9104/trainers' , params = {'trainer_id' : '4186'})
    assert response1.json() ["trainer_name"] == 'Лиза'

