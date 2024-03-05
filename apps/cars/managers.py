from django.db import models


class CarsManager(models.Manager):
    def get_only_specific_brand(self, brand):
        return self.filter(brand=brand)
