import folium
import json

from django.http import HttpResponseNotFound
from django.shortcuts import render
from django.utils import timezone

from .models import PokemonEntity, Pokemons


MOSCOW_CENTER = [55.751244, 37.618423]
DEFAULT_IMAGE_URL = (
    'https://vignette.wikia.nocookie.net/pokemon/images/6/6e/%21.png/revision'
    '/latest/fixed-aspect-ratio-down/width/240/height/240?cb=20130525215832'
    '&fill=transparent'
)


def add_pokemon(folium_map, lat, lon, image_url=DEFAULT_IMAGE_URL):
    icon = folium.features.CustomIcon(
        image_url,
        icon_size=(50, 50),
    )
    folium.Marker(
        [lat, lon],
        # Warning! `tooltip` attribute is disabled intentionally
        # to fix strange folium cyrillic encoding bug
        icon=icon,
    ).add_to(folium_map)


def show_all_pokemons(request):
    time_now = timezone.now()
    time_new = timezone.localtime(time_now)
    pokemon_entities = PokemonEntity.objects.filter(appeared_at__lt=time_new, disappeared_at__gt=time_new)
    
    folium_map = folium.Map(location=MOSCOW_CENTER, zoom_start=12)
    for pokemon_entity in pokemon_entities:
        try:
            relative_image_path = pokemon_entity.name.image.url
            absolute_uri = request.build_absolute_uri(relative_image_path)
        except ValueError:
            absolute_uri = request.build_absolute_uri()
        add_pokemon(
            folium_map, pokemon_entity.lat,
            pokemon_entity.lon,
            absolute_uri
        )

    pokemons_on = Pokemons.objects.all()
    pokemons_on_page = []
    for pokemon in pokemons_on:
        try:
            relative_image_path = pokemon.image.url
            absolute_uri = request.build_absolute_uri(relative_image_path)
        except ValueError:
            absolute_uri = request.build_absolute_uri()
        pokemons_on_page.append({
            'pokemon_id': pokemon.id,
            'img_url': absolute_uri,
            'title_ru': pokemon.title,
        })

    return render(request, 'mainpage.html', context={
        'map': folium_map._repr_html_(),
        'pokemons': pokemons_on_page,
    })


def show_pokemon(request, pokemon_id):
    pokemon_entity = PokemonEntity.objects.get(id=pokemon_id)
    
    relative_image_path = pokemon_entity.name.image.url
    absolute_uri = request.build_absolute_uri(relative_image_path)

    folium_map = folium.Map(location=MOSCOW_CENTER, zoom_start=12)
    pokemon = {
        "pokemon_id": pokemon_entity.name.id,
        "title_ru": pokemon_entity.name.title,
        "description": pokemon_entity.name.description,
        "img_url": absolute_uri
    }
    add_pokemon(
                folium_map, pokemon_entity.lat,
                pokemon_entity.lon,
                absolute_uri,
            )

    return render(request, 'pokemon.html', context={
        'map': folium_map._repr_html_(), 'pokemon': pokemon
    })
