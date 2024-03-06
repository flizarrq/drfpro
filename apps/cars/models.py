from django.core import validators as V
from django.db import models

from core.enums.regex_enum import Regex
from core.models import BaseModel

from apps.auto_parks.models import AutoParksModel

from .managers import CarsManager


class CarsModel(BaseModel):
    class Meta:
        db_table = 'cars'
        ordering = ['-id']

    brand = models.CharField(max_length=20, validators=[V.RegexValidator(*Regex.BRAND.value)])
    price = models.IntegerField()
    year = models.IntegerField()
    auto_park = models.ForeignKey(AutoParksModel, on_delete=models.CASCADE, related_name='cars')

    objects = CarsManager()
