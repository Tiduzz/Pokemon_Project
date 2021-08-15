from django.shortcuts import render
from core.models import *
from pokemons import *
# Create your views here.

data_pokemon = pokemons_names()

def index(request):
    return render(request, 'index.html', { 'data_pokemon' : data_pokemon })

def pokedex(request):
    if request.POST:
        pokemon = {'pokemon_name' : request.POST.get('Pokemons')}
    poke_desc = pokemons_description(pokemon)
    pokemon = {'pokemon_name' : pokemon}
    data_pokemon.update(pokemon)
    data_pokemon.update(poke_desc)
    return render(request, 'pokedex.html', { 'data_pokemon' : data_pokemon })