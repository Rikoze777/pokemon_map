from email.utils import localtime
import folium

from django.shortcuts import render, get_object_or_404
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
    time_now = localtime()
    pokemon_entities = PokemonEntity.objects.filter(appeared_at__lt=time_now,
                                                disappeared_at__gt=time_now)
    folium_map = folium.Map(location=MOSCOW_CENTER, zoom_start=12)
    pokemons_on_page = []
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
        pokemons_on_page.append({
            'pokemon_id': pokemon_entity.name.id,
            'img_url': absolute_uri,
            'title_ru': pokemon_entity.name.title,
        })

    return render(request, 'mainpage.html', context={
        'map': folium_map._repr_html_(),
        'pokemons': pokemons_on_page,
    })


def show_pokemon(request, pokemon_id):
    time_now = localtime()

    pokemon = get_object_or_404(Pokemons, id=pokemon_id)

    requested_pokemon = {
        "title_ru": pokemon.title,
        "title_en": pokemon.title_en,
        "title_jp": pokemon.title_jp,
        "img_url": request.build_absolute_uri(pokemon.image.url),
        "description": pokemon.description,
        "entities": pokemon.entities.filter(
            appeared_at__lt=time_now, disappeared_at__gt=time_now
        ).values(),
    }

    if pokemon.previous_evolution:
        requested_pokemon["previous_evolution"] = {
            "title_ru": pokemon.previous_evolution.title,
            "pokemon_id": pokemon.previous_evolution.id,
            "img_url": request.build_absolute_uri(
                pokemon.previous_evolution.image.url
            ),
        }

    next_evolution = pokemon.next_evolutions.first()

    if next_evolution:
        requested_pokemon["next_evolution"] = {
            "title_ru": next_evolution.title,
            "pokemon_id": next_evolution.id,
            "img_url": request.build_absolute_uri(next_evolution.image.url),
        }
    folium_map = folium.Map(location=MOSCOW_CENTER, zoom_start=12)

    for entity in requested_pokemon["entities"]:
        add_pokemon(
            folium_map,
            entity["lat"],
            entity["lon"],
            requested_pokemon["img_url"],
        )

    return render(request, 'pokemon.html', context={
        'map': folium_map._repr_html_(), 'pokemon': requested_pokemon
    })
