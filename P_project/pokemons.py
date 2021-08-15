import requests
import pokepy


#returns all 151 pokemons as a dict {'pokemon_name':'Pokemon_name'}
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
    poke_description = {'description' : poke_desc}
    return poke_desc