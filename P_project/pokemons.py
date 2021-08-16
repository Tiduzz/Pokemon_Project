import requests
import pokepy
import pandas as pd


#returns all 151 pokemons as a dict {'pokemon_name':'Pokemon_name'}
def pokemons_names():
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
        try:
            x = {}
            x = {'type{}'.format(i) : result.types[i].type.name.capitalize()}
            pokemon_types.update(x)
        except IndexError:
            pass
    return pokemon_types

def pokemons_png(pokemon):
    result = requests.get('https://pokeapi.co/api/v2/pokemon/{}/'.format(pokemon))
    result = result.json()
    return result['sprites']['front_default']

def pokemons_weakness(pokemon):
    type_weaknesses = {'Fairy' : {'Poison', 'Steel'} }, {'Steel' : {'Fire', 'Fight', 'Ground'} }, {'Dark' : {'Fire', 'Bug', 'Fairy'} }, {'Dragon' : {'Ice', 'Dragon', 'Fairy' }}, {'Ghost' : {'Ghost', 'Dark'} }, {'Rock' : {'Water', 'Grass', 'Fight', 'Ground', 'Steel'}}, {'Bug' : {'Fire', 'Flying', 'Rock'} }, {'Psychic' : {'Bug', 'Ghost', 'Dark'} }, {'Flying' : {'Electric', 'Ice', 'Rock'} }, {'Ground' : {'Water', 'Grass', 'Ice'} }, {'Poison' : {'Ground', 'Psychic'} }, {'Fight' : {'Flying', 'Psychic', 'Fairy'} }, {'Ice' : {'Fire', 'Fight', 'Rock', 'Steel'} }, {'Grass' : {'Fire', 'Ice', 'Poison', 'Flying', 'Bug'} }, {'Electric' : {'Ground'} }, {'Water' : {'Electric', 'Grass'} }, {'Fire' : {'Water', 'Ground', 'Rock'} }, {'Normal' : {'Fight'} }
    poke_type = pokemons_types(pokemon)
    type0 = poke_type['type0']
    try:
        type1 = poke_type['type1']
        type0_weak = ''
        type1_weak = ''
        double_weak = []
        count = 0
        for i in type_weaknesses:
            for key,value in i.items():
                if type0 == key:
                    type0_weak = value
                if type1 == key:
                    type1_weak = value
        for i in type0_weak:
            for y in type1_weak:
                if i == y:
                    double_weak.append(i)
        pokemon_weak = list(type1_weak)
        for i in list(type0_weak):
            pokemon_weak.append(i)
        pokemon_weak = pd.unique(pokemon_weak).tolist()
        for i in double_weak:
            pokemon_weak.remove(i)
            pokemon_weak.append(i+" x4 DMG!")
        return pokemon_weak

    except KeyError:
        type0_weak = ''
        count = 0
        for i in type_weaknesses:
            for key,value in i.items():
                if type0 == key:
                    type0_weak = value
        return list(type0_weak)