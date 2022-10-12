from django.db import models


class Pokemons(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200, verbose_name='Название покемона')
    title_en = models.CharField(max_length=200, null=True, verbose_name='Название покемона на английском')
    title_jp = models.CharField(max_length=200, null=True, verbose_name='Название покемона на японском')
    description = models.TextField(blank=True, null=True, verbose_name='Описание покемона')
    image = models.ImageField(upload_to='image', blank=True, verbose_name='Изображение покемона')
    previous_evolution = models.ForeignKey("self", on_delete=models.SET_NULL, null=True, related_name="next_evolutions", verbose_name='Из кого эволюционирует')

    def __str__(self):
        return self.title


class PokemonEntity(models.Model):
    name = models.ForeignKey(Pokemons, null=True, on_delete=models.SET_NULL, related_name="entities", verbose_name='Связь с моделью покемона')
    lat = models.FloatField(blank=True, verbose_name='Широта')
    lon = models.FloatField(blank=True, verbose_name='Долгота')
    appeared_at = models.DateTimeField(blank=True, null=True, verbose_name='Время появления')
    disappeared_at = models.DateTimeField(blank=True, null=True, verbose_name='Время исчезновения')
    level = models.IntegerField(blank=True, null=True, verbose_name='Уровень')
    health = models.IntegerField(blank=True, null=True, verbose_name='Здоровье')
    strength = models.IntegerField(blank=True, null=True, verbose_name='Сила')
    defence = models.IntegerField(blank=True, null=True, verbose_name='Защита')
    stamina = models.IntegerField(blank=True, null=True, verbose_name='Выносливость')


    def __str__(self):
        return f"{self.name}  lat-{self.lat}  lon-{self.lon}"
