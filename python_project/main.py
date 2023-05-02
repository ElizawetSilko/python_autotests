import requests

#Создать покемона
response = requests.post('https://pokemonbattle.me:9104/pokemons' , headers={'trainer_token':'4b73c485e194de4704b4c76474ae9052'} , json={
    "name":"Spider",
    "photo": "https://dolnikov.ru/pokemons/albums/008.png",
    "stage": 2,
    "attack": 1})

print(response.text)

#Поменять имя
response = requests.put('https://pokemonbattle.me:9104/pokemons' , headers={'trainer_token':'4b73c485e194de4704b4c76474ae9052'} , json={
    "pokemon_id": 9721,
    "name": "New Name",
    "photo": "https://dolnikov.ru/pokemons/albums/008.png"})

print(response.text)


#Поймать покемона
response = requests.post('https://pokemonbattle.me:9104/trainers/add_pokeball' , headers={'trainer_token':'4b73c485e194de4704b4c76474ae9052'} , json={
    "pokemon_id": 9721,
})

print(response.text)