from rest_framework import serializers

from apps.auto_cars.serializers import AutoParksWithoutCarsSerializer

from .models import UserModel


class UserSerializer(serializers.ModelSerializer):
    auto_parks = AutoParksWithoutCarsSerializer(many=True, read_only=True)

    class Meta:
        model = UserModel
        fields = ('id', 'name', 'age', 'created_at', 'updated_at', 'auto_parks')
