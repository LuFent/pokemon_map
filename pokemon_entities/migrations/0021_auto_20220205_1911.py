# Generated by Django 2.2.5 on 2022-02-05 16:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pokemon_entities', '0020_auto_20220203_1445'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pokemonentity',
            name='pokemon_type',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='entities', to='pokemon_entities.Pokemon', verbose_name='К какому виду пренадлежит'),
        ),
    ]
