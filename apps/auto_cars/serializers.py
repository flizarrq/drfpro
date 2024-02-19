from rest_framework import serializers

from apps.cars.serializers import CarSerializer

from .models import AutoParksModel


class AutoParkSerializer(serializers.ModelSerializer):
    cars = CarSerializer(many=True, read_only=True)

    class Meta:
        model = AutoParksModel
        fields = ('id', 'name', 'created_at', 'updated_at', 'cars')
