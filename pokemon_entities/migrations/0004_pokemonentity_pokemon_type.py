# Generated by Django 3.1.14 on 2022-02-01 12:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pokemon_entities', '0003_auto_20220201_1504'),
    ]

    operations = [
        migrations.AddField(
            model_name='pokemonentity',
            name='pokemon_type',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='pokemon_entities.pokemon'),
        ),
    ]
