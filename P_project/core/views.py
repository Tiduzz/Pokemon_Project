from django.shortcuts import render
from core.models import *
from pokemons import *
# Create your views here.

def index(request):
    data_pokemon = pokemons()
    return render(request, 'index.html', { 'data_pokemon' : data_pokemon})

# def index(request):
#     dados_pokemons = pokemons()
#     return render(request, 'index.html', dados_pokemons)