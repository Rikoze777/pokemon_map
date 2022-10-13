# Generated by Django 4.0.5 on 2022-10-12 19:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pokemon_entities', '0019_alter_pokemonentity_appeared_at_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pokemonentity',
            name='name',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='entities', to='pokemon_entities.pokemons', verbose_name='Связь с моделью покемона'),
        ),
    ]