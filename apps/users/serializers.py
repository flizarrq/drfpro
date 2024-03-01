from django.contrib.auth import get_user_model

from rest_framework import serializers

UserModel = get_user_model()
from .models import ProfileModel


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProfileModel
        fields = (
            'id', 'name', 'surname', 'age'
        )


class UserSerializer(serializers.ModelSerializer):
    profile = ProfileSerializer()

    class Meta:
        model = UserModel
        fields = (
            'id', 'email', 'password', 'is_active', 'is_staff', 'is_superuser',
            'last_login', 'updated_at', 'created_at', 'profile'
        )
        read_only_fields = (
            'id', 'is_active', 'is_staff', 'is_superuser',
            'last_login', 'updated_at', 'created_at'
        )
        extra_kwargs = {
            'password': {
                'write_only': True
            }
        }

    def create(self, validated_data):
        profile = validated_data.pop('profile')
        user = UserModel.objects.create_user(**validated_data)
        ProfileModel.objects.create(**profile, user=user)
        return user
