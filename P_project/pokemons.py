import requests
import pokepy


#returns all 151 pokemons as a dict {'pokemon_name':'Pokemon_name'}
def pokemons_names():
    response = requests.get('https://pokeapi.co/api/v2/pokemon?limit=3')
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

# returns description of male pokemon. Only accepts str (as 'pokemon_name') or int (number 1 ~ 151)
def pokemons_description(pokemon):
    description = pokepy.V2Client().get_pokemon_species(pokemon).flavor_text_entries[0].flavor_text
    description = description.replace("\n", " ")
    poke_desc = ''
    for i in description:
        poke_desc += i
        if i == '.':
            break
    return poke_desc

def pokemons_stats(pokemon):
    result = pokepy.V2Client().get_pokemon(pokemon)
    base_stats = {}
    for i in range(6):
        change_name = result.stats[i].stat.name
        L = ''
        for letter in change_name:
            if letter == '-':
                continue
            else:
                L += letter
        x = {}
        x = {L : result.stats[i].base_stat}
        base_stats.update(x)
    return base_stats

def pokemons_types(pokemon):
    result = pokepy.V2Client().get_pokemon(pokemon)
    pokemon_types = {}
    for i in range(2):
        x = {}
        x = {'type{}'.format(i) : result.types[i].type.name.capitalize()}
        pokemon_types.update(x)
    return pokemon_types

def pokemons_png(pokemon):
    result = requests.get('https://pokeapi.co/api/v2/pokemon/{}/'.format(pokemon))
    result = result.json()
    return result['sprites']['front_default']