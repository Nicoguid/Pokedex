from django.shortcuts import render #HTML
from .models import Pokemon
from .services import fetch_and_save_pokemon

# Create your views here.
def index(request):
    if Pokemon.objects.count() < 50:
        fetch_and_save_pokemon()
    lista_pokemons = Pokemon.objects.all()   
    return render(request, 'pokedex/index.html', {'pokemon_list': lista_pokemons})

def filtro_peso(request):
    lista_pokemons = Pokemon.objects.filter(peso__gt=30, peso__lt=80)
    return render(request, 'pokedex/filtro_peso.html', {'pokemon_list': lista_pokemons})

def filtro_tipo(request):
    lista_pokemons = Pokemon.objects.filter(tipos__icontains='grass')
    return render(request, 'pokedex/filtro_tipo.html', {'pokemon_list': lista_pokemons})

def filtro_combinado(request):
    lista_pokemons = Pokemon.objects.filter(tipos__icontains='flying', altura__gt=10)
    return render(request, 'pokedex/filtro_combinado.html', {'pokemon_list': lista_pokemons})

def transformacion(request):
    pokemons = Pokemon.objects.all()
    lista_pokemons = [{'nombre': p.nombre, 'nombre_invertido': p.nombre[::-1]} for p in pokemons]
    return render(request, 'pokedex/invertidos.html', {'pokemon_list': lista_pokemons})