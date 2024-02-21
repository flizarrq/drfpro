from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from .models import CarModel


class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarModel
        fields = ('id', 'brand', 'price', 'year', 'created_at', 'updated_at', 'auto_park_id')


