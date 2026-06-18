from django.db import models

# Create your models here.

class Pokemon(models.Model):
    pokemon_id = models.IntegerField(unique=True)
    nombre = models.CharField(max_length=100)
    tipos = models.CharField(max_length=200)
    altura = models.IntegerField()
    peso = models.IntegerField()

    def __str__(self):
        return self.nombre