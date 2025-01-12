# Generated by Django 4.0.5 on 2022-10-13 16:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pokemon_entities', '0022_alter_pokemonentity_appeared_at_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pokemons',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='pokemons',
            name='previous_evolution',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='next_evolutions', to='pokemon_entities.pokemons', verbose_name='Прошлая эволюция'),
        ),
    ]
