# Generated by Django 4.0.5 on 2022-10-12 16:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pokemon_entities', '0013_pokemons_title_en_pokemons_title_jp'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pokemonentity',
            name='name',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='pokemon_entities.pokemons'),
        ),
        migrations.CreateModel(
            name='PreviousEvolution',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='pokemon_entities.previousevolution')),
            ],
        ),
        migrations.CreateModel(
            name='NextEvolution',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='pokemon_entities.nextevolution')),
            ],
        ),
    ]
