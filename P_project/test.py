import requests
import pokepy



# def pokemons_type(pokemon):
#     result = pokepy.V2Client().get_pokemon(pokemon)
#     pokemon_types = {}
#     for i in range(2):
#         x = {}
#         x = {'type{}'.format(i) : result.types[i].type.name}
#         pokemon_types.update(x)
#     return pokemon_types

def pokemons_png(pokemon):
    result = requests.get('https://pokeapi.co/api/v2/pokemon/{}/'.format(pokemon))
    result = result.json()
    return result['sprites']['front_default']
print (pokemons_png(1))