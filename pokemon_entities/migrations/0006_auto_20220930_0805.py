# Generated by Django 2.2.24 on 2022-09-30 08:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pokemon_entities', '0005_auto_20220930_0801'),
    ]

    operations = [
        migrations.AddField(
            model_name='pokemonentity',
            name='defence',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='pokemonentity',
            name='dtamina',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='pokemonentity',
            name='health',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='pokemonentity',
            name='level',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='pokemonentity',
            name='strength',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]