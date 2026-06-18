from django.db import models

class Pokemon(models.Model):
    """
    Modelo que representa un pokemon obtenido de la PokeAPI. Cada instancia corresponde a una fila en la base de datos
    """
    pokemon_id = models.IntegerField(unique=True)  # ID de la Pokedex
    nombre = models.CharField(max_length=100)       # Nombre del pokemon
    tipos = models.CharField(max_length=200)        # Tipos del pokemon separados por coma
    altura = models.IntegerField()                  # Altura del pokemon
    peso = models.IntegerField()                    # Peso del pokemon
    imagen = models.URLField(max_length=200, blank=True)  # URL de la imagen

    def __str__(self) -> str:
        return self.nombre