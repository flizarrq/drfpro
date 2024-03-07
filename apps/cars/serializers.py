from rest_framework import serializers

from .models import CarsModel


class CarsSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarsModel
        fields = ('id', 'brand', 'price', 'year', 'body_type', 'created_at', 'updated_at')
