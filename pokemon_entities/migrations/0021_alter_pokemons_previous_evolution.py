# Generated by Django 4.0.5 on 2022-10-12 19:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pokemon_entities', '0020_alter_pokemonentity_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pokemons',
            name='previous_evolution',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='next_evolutions', to='pokemon_entities.pokemons', verbose_name='Из кого эволюционирует'),
        ),
    ]
