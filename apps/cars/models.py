from django.core import validators as V
from django.db import models

from core.enums.regex_enum import Regex
from core.models import BaseModel

from apps.auto_parks.models import AutoParksModel

from .managers import CarsManager

from .choises.body_type_choices import BodyTypeChoices


class CarsModel(BaseModel):
    class Meta:
        db_table = 'cars'
        ordering = ['-id']

    brand = models.CharField(max_length=20, validators=[V.RegexValidator(*Regex.BRAND.value)])
    price = models.IntegerField()
    year = models.IntegerField()
    body_type = models.CharField(max_length=10, choices=BodyTypeChoices.choices)
    # auto_park = models.ForeignKey(AutoParksModel, on_delete=models.CASCADE, related_name='cars')

    objects = CarsManager()
