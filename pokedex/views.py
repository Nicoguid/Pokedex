from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from .models import Pokemon
from .services import fetch_and_save_pokemon

def index(request: HttpRequest) -> HttpResponse:
    """
    Vista principal. Carga los pokemon desde la API si la base de datos tiene menos de 50 registros, y muestra la tabla completa
    """
    if Pokemon.objects.count() < 50:
        fetch_and_save_pokemon()
    lista_pokemons = Pokemon.objects.all()
    return render(request, 'pokedex/index.html', {'pokemon_list': lista_pokemons})

def filtro_peso(request: HttpRequest) -> HttpResponse:
    """
    Filtra los pokemon con peso mayor a 30 y menor a 80
    """
    lista_pokemons = Pokemon.objects.filter(peso__gt=30, peso__lt=80)
    return render(request, 'pokedex/filtro_peso.html', {'pokemon_list': lista_pokemons})

def filtro_tipo(request: HttpRequest) -> HttpResponse:
    """
    Filtra los pokemon de tipo grass
    """
    lista_pokemons = Pokemon.objects.filter(tipos__icontains='grass')
    return render(request, 'pokedex/filtro_tipo.html', {'pokemon_list': lista_pokemons})

def filtro_combinado(request: HttpRequest) -> HttpResponse:
    """
    Filtra los pokemon de tipo flying que midan mas de 10
    """
    lista_pokemons = Pokemon.objects.filter(tipos__icontains='flying', altura__gt=10)
    return render(request, 'pokedex/filtro_combinado.html', {'pokemon_list': lista_pokemons})

def transformacion(request: HttpRequest) -> HttpResponse:
    """
    Muestra todos los pokemon con sus nombres invertidos
    """
    pokemons = Pokemon.objects.all()
    lista_pokemons = [{'nombre': p.nombre, 'nombre_invertido': p.nombre[::-1]} for p in pokemons]
    return render(request, 'pokedex/invertidos.html', {'pokemon_list': lista_pokemons})