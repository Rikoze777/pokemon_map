# Generated by Django 4.0.5 on 2022-10-12 17:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pokemon_entities', '0016_alter_pokemons_next_evolution_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pokemons',
            name='next_evolution',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='next', to='pokemon_entities.pokemons'),
        ),
        migrations.AlterField(
            model_name='pokemons',
            name='previous_evolution',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='previous', to='pokemon_entities.pokemons'),
        ),
    ]
