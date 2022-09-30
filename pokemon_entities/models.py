from django.db import models


class Pokemons(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='image', blank=True)

    def __str__(self):
        return self.title


class PokemonEntity(models.Model):
    lat = models.FloatField(blank=True)
    lon = models.FloatField(blank=True)
