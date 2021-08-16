import requests
import pokepy



def pokemons_names():
    response = requests.get('https://pokeapi.co/api/v2/pokemon?limit=5')
    response = response.json()

    results = response['results']
    poke_names = []
    for dict in results:
        for key in dict:
            if key == 'name':
                poke_names.append(dict[key])

    data_pokemon = {}
    for pokemon in poke_names:
        x = {'name' : pokemon.capitalize()}
        data_pokemon.update(x)
    return data_pokemon

print (pokemons_names())