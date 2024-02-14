from rest_framework import serializers

from .models import CarModel


class CarSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    year = serializers.IntegerField()
    brand = serializers.CharField(max_length=20)
    seat_count = serializers.IntegerField()
    body_type = serializers.CharField(max_length=20)
    engine_volume = serializers.FloatField()

    def create(self, validated_data):
        car = CarModel.objects.create(**validated_data)
        return car

    def update(self, instance, validated_data):
        for k, v in validated_data.items():
            setattr(instance, k, v)

        instance.save()
        return instance
