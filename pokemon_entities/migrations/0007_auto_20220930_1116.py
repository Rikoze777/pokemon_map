# Generated by Django 2.2.24 on 2022-09-30 11:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pokemon_entities', '0006_auto_20220930_0805'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pokemons',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
