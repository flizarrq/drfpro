from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.core import validators as V
from django.db import models

from core.enums.regex_enum import Regex
from core.models import BaseModel

from .managers import UserManager


class UserModel(AbstractBaseUser, PermissionsMixin, BaseModel):
    class Meta:
        db_table = 'auth_user'

    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'

    objects = UserManager()


class ProfileModel(BaseModel):
    class Meta:
        db_table = 'profile'

    name = models.CharField(max_length=20, validators=[V.RegexValidator(*Regex.NAME.value)])
    surname = models.CharField(max_length=20, validators=[V.RegexValidator(*Regex.NAME.value)])
    age = models.IntegerField(validators=[V.MinValueValidator(16), V.MaxValueValidator(150)])
    user = models.OneToOneField(UserModel, on_delete=models.CASCADE, related_name='profile')
