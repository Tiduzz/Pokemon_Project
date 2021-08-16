from django.shortcuts import render
from core.models import *
from pokemons import *
# Create your views here.

data_pokemon = pokemons_names()

def index(request):
    return render(request, 'index.html', { 'data_pokemon' : data_pokemon })

def pokedex(request):
    if request.POST:
        pokemon = {'pokemon_name' : request.POST.get('poke')}
        poke_desc = {'pokemon_description' : pokemons_description(request.POST.get('poke'))}
        poke_stats = {'pokemon_base_status' : pokemons_stats(request.POST.get('poke'))}
        poke_types = {'pokemon_types' : pokemons_types(request.POST.get('poke'))}
        poke_png = {'pokemon_png' : pokemons_png(request.POST.get('poke'))}
        poke_weak = {'pokemon_weakness' : pokemons_weakness(request.POST.get('poke'))}
    data_pokemon.update(pokemon)
    data_pokemon.update(poke_desc)
    data_pokemon.update(poke_stats)
    data_pokemon.update(poke_types)
    data_pokemon.update(poke_png)
    data_pokemon.update(poke_weak)
    return render(request, 'pokedex.html', { 'data_pokemon' : data_pokemon })