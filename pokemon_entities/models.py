from django.db import models


class Pokemons(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='image', blank=True)

    def __str__(self):
        return self.title


class PokemonEntity(models.Model):
    name = models.ForeignKey(Pokemons, null=True, on_delete=models.SET_NULL)
    lat = models.FloatField(blank=True)
    lon = models.FloatField(blank=True)
    appeared_at = models.DateTimeField(blank=True, null=True)
    disappeared_at = models.DateTimeField(blank=True, null=True)
    level = models.IntegerField(blank=True, null=True)
    health = models.IntegerField(blank=True, null=True)
    strength = models.IntegerField(blank=True, null=True)
    defence = models.IntegerField(blank=True, null=True)
    dtamina = models.IntegerField(blank=True, null=True)
