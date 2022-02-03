from django.db import models  # noqa F401


class Pokemon(models.Model):
    title_ru = models.CharField(max_length=200, null=True)
    title_jp = models.CharField(max_length=200, null=True)
    title_en = models.CharField(max_length=200, null=True)
    img = models.ImageField(null=True)
    description = models.TextField(null=True)
    previous_evolution = models.ForeignKey("self",
                                           on_delete=models.CASCADE,
                                           null=True,
                                           related_name="next_evolution")

    def __str__(self):
        return self.title_ru


class PokemonEntity(models.Model):
    latitude = models.FloatField()
    longitude = models.FloatField()
    pokemon_type = models.ForeignKey(Pokemon,
                                     on_delete=models.CASCADE,
                                     default=None)
    appeared_at = models.DateField(default=None)
    disappeared_at = models.DateField(default=None)
    level = models.IntegerField(default=0)
    health = models.IntegerField(default=0)
    strength = models.IntegerField(default=0)
    defence = models.IntegerField(default=0)
    stamina = models.IntegerField(default=0)

    def __str__(self):
        return 'Особь ' + self.pokemon_type.title_ru