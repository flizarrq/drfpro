from django.http import QueryDict
from django.db.models import QuerySet
from django.core.exceptions import ValidationError

from .models import CarModel


def cars_filter(query: QueryDict) -> QuerySet:
    qs = CarModel.objects.all()
    for k, v in query.items():
        match k:
            case 'price_gt':
                qs = qs.filter(price__gt=v)
            case 'price_lt':
                qs = qs.filter(price__gt=v)
            case _:
                raise ValidationError({'detail:' f'{k}  is not allowed here'})
    return qs
