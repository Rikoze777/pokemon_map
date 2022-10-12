from django.db import models


class Pokemons(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    title_en = models.CharField(max_length=200, null=True)
    title_jp = models.CharField(max_length=200, null=True)
    description = models.TextField(blank=True, null=True)
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
    stamina = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return f"{self.name}  lat-{self.lat}  lon-{self.lon}"
