from django.db import models


class CarManager(models.Manager):
    def get_only_by_brand(self, name):
        return self.filter(brand=name)
