from django.db import models  # noqa F401


class Pokemon(models.Model):
    title_ru = models.CharField("Название покемона на русском", max_length=200, default="")
    title_jp = models.CharField("Название покемона на японском", max_length=200, default="")
    title_en = models.CharField("Название покемона на английском", max_length=200, default="")
    img = models.ImageField("Изображение покемона", null=True)
    description = models.TextField("Описание покемона на русском", default="")
    previous_evolution = models.ForeignKey("self",
                                           on_delete=models.CASCADE,
                                           null=True,
                                           verbose_name="Из какого вида эволюционировал",
                                           related_name="next_evolution",
                                           blank=True)

    def __str__(self):
        return self.title_ru


class PokemonEntity(models.Model):
    latitude = models.FloatField("Широта")
    longitude = models.FloatField("Долгота")
    pokemon_type = models.ForeignKey(Pokemon,
                                     on_delete=models.CASCADE,
                                     verbose_name="К какому виду пренадлежит",
                                     default=None)
    appeared_at = models.DateField("Дата появления", null=True, blank=True)
    disappeared_at = models.DateField("Дата изчезновения", null=True, blank=True)
    level = models.IntegerField("Уровень", null=True, blank=True)
    health = models.IntegerField("Здоровье", null=True, blank=True)
    strength = models.IntegerField("Сила", null=True, blank=True)
    defence = models.IntegerField("Защита", null=True, blank=True)
    stamina = models.IntegerField("Выносливость", null=True, blank=True)

    def __str__(self):
        return 'Особь ' + self.pokemon_type.title_ru