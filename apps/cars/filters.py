from django.http import QueryDict
from django.db.models import QuerySet
from django.core.exceptions import ValidationError

from .models import CarModel
from .serializers import CarSerializer


def cars_filter(query: QueryDict) -> QuerySet:
    qs = CarModel.objects.all()
    for k, v in query.items():
        match k:
            case 'price_gt':
                qs = qs.filter(price__gt=v)
            case 'price_lt':
                qs = qs.filter(price__gt=v)
            case 'price_gte':
                qs = qs.filter(price__gte=v)
            case 'price_lte':
                qs = qs.filter(price__gte=v)

            case 'year_gt':
                qs = qs.filter(year__gt=v)
            case 'year_lt':
                qs = qs.filter(year__gt=v)
            case 'year_gte':
                qs = qs.filter(year__gte=v)
            case 'year_lte':
                qs = qs.filter(year__gte=v)

            case 'brand_start':
                qs = qs.filter(brand__istartswith=v)
            case 'brand_end':
                qs = qs.filter(brand__iendswith=v)
            case 'brand_contains':
                qs = qs.filter(brand__icontains=v)

            case 'order':
                fields = CarSerializer.Meta.fields
                fields = [*fields, *[f'-{field}' for field in fields]]

                if v not in fields:
                    raise ValidationError({'detail:' f'Please choose order from {",".join(fields)}'})
                qs = qs.order_by(v)

            case _:
                raise ValidationError({'detail:' f'{k}  is not allowed here'})
    return qs
