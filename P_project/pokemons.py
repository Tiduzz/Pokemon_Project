import requests


def pokemons():
    response = requests.get('https://pokeapi.co/api/v2/pokemon?limit=151')
    response = response.json()

    results = response['results']
    poke_names = []
    for dict in results:
        for key in dict:
            if key == 'name':
                poke_names.append(dict[key])

    data_pokemon = {}
    for pokemon in poke_names:
        x = {str(pokemon) : pokemon.capitalize()}
        data_pokemon.update(x)
    return data_pokemon

if __name__ == '__main__':
    print (pokemons())

    # cap_poke_names = []
    # for pokemon in poke_names:
    #     cap_poke_names.append(pokemon.capitalize())
    # return cap_poke_names