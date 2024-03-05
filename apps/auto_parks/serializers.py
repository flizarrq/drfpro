from rest_framework import serializers

from .models import AutoParksModel


class AutoParkSerializer(serializers.ModelSerializer):
    class Meta:
        model = AutoParksModel
        fields = ('id', 'name', 'created_at', 'updated_at')
