import requests
from .models import Pokemon

def fetch_and_save_pokemon() -> None:
    """
    Busca y guarda los primeros 50 pokemon de la PokeAPI y los guarda en la base de datos
    """
    url: str = "https://pokeapi.co/api/v2/pokemon?limit=50"
    
    try:
        buscador = requests.get(url, timeout=10)
        buscador.raise_for_status()
        datos = buscador.json()
    except requests.exceptions.RequestException as e:
        print(f"Error al conectar con la PokeAPI: {e}")
        return

    for item in datos["results"]:
        try:
            # Busca el detalle individual de cada Pokemon
            detalle = requests.get(item["url"], timeout=10).json()

            pokemon_id: int = detalle["id"]
            nombre: str = detalle["name"]
            tipos: str = ", ".join([t["type"]["name"] for t in detalle["types"]])
            altura: int = detalle["height"]
            peso: int = detalle["weight"]
            imagen: str = detalle["sprites"]["front_default"] or ""

            # Guarda o actualiza el Pokemon en la base de datos
            Pokemon.objects.update_or_create(
                pokemon_id=pokemon_id,
                defaults={
                    "nombre": nombre,
                    "tipos": tipos,
                    "altura": altura,
                    "peso": peso,
                    "imagen": imagen,
                }
            )
        except Exception as e:
            print(f"Error al procesar {item['url']}: {e}")
            continue