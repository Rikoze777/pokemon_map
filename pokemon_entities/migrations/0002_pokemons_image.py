# Generated by Django 2.2.24 on 2022-09-29 20:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pokemon_entities', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='pokemons',
            name='image',
            field=models.ImageField(blank=True, upload_to='image'),
        ),
    ]
