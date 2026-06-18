import requests
from .models import Pokemon

def fetch_and_save_pokemon():
    url = "https://pokeapi.co/api/v2/pokemon?limit=50"
    buscador = requests.get(url)
    datos = buscador.json()

    for item in datos["results"]:
        detalle = requests.get(item["url"]).json()

        pokemon_id = detalle["id"]
        nombre = detalle["name"]
        tipos = ", ".join([t["type"]["name"] for t in detalle["types"]])
        altura = detalle["height"]
        peso = detalle["weight"]

        Pokemon.objects.update_or_create(
            pokemon_id=pokemon_id,
            defaults={
                "nombre": nombre,
                "tipos": tipos,
                "altura": altura,
                "peso": peso,
            }
        )