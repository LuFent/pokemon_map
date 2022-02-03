import folium
import json

from .models import Pokemon, PokemonEntity
from django.http import HttpResponseNotFound, HttpRequest
from django.shortcuts import render


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
    pokemons = Pokemon.objects.all()
    folium_map = folium.Map(location=MOSCOW_CENTER, zoom_start=12)

    for pokemon in pokemons:
        if pokemon.img:
            image_path = pokemon.img.url
        else:
            image_path = None

        for pokemon_entity in PokemonEntity.objects.filter(pokemon_type=pokemon):
            add_pokemon(
                folium_map, pokemon_entity.latitude,
                pokemon_entity.longitude,
                request.build_absolute_uri(image_path)
            )

    pokemons_on_page = []
    for pokemon in pokemons:
        if pokemon.img:
            image_path = pokemon.img.url
        else:
            image_path = None

        pokemons_on_page.append({
            'pokemon_id': pokemon.id,
            'img_url': request.build_absolute_uri(image_path),
            'title_ru': pokemon.title_ru,
        })

    return render(request, 'mainpage.html', context={
        'map': folium_map._repr_html_(),
        'pokemons': pokemons_on_page,
    })


def show_pokemon(request, pokemon_id):
    requested_pokemon = Pokemon.objects.get(id=pokemon_id)

    if requested_pokemon.img:
        image_path = request.build_absolute_uri(requested_pokemon.img.url)
    else:
        image_path = None

    folium_map = folium.Map(location=MOSCOW_CENTER, zoom_start=12)
    for pokemon_entity in PokemonEntity.objects.filter(pokemon_type=requested_pokemon):
        add_pokemon(
            folium_map, pokemon_entity.latitude,
            pokemon_entity.longitude,
            image_path)

    if requested_pokemon.previous_evolution:
        previous_pokemon = {"img_url": request.build_absolute_uri(requested_pokemon.previous_evolution.img.url),
                            "title_ru": requested_pokemon.previous_evolution.title_ru,
                            "pokemon_id": requested_pokemon.previous_evolution.id}
    else:
        previous_pokemon = None

    try:
        next_pokemon_obj = requested_pokemon.next_evolution.get()
        next_pokemon = {"img_url": request.build_absolute_uri(next_pokemon_obj.img.url),
                        "title_ru": next_pokemon_obj.title_ru,
                        "pokemon_id": next_pokemon_obj.id}

    except Pokemon.DoesNotExist:
        next_pokemon = None

    return render(request, 'pokemon.html', context={
                    'map': folium_map._repr_html_(),
                    'pokemon': {'img_url': image_path,
                                'title_ru': requested_pokemon.title_ru,
                                'title_jp': requested_pokemon.title_jp,
                                'title_en': requested_pokemon.title_en,
                                'description': requested_pokemon.description,
                                'previous_evolution': previous_pokemon,
                                'next_evolution': next_pokemon
                                }})