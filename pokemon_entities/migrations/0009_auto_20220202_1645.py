# Generated by Django 3.1.14 on 2022-02-02 13:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pokemon_entities', '0008_pokemon_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pokemon',
            old_name='title',
            new_name='title_ru',
        ),
    ]
