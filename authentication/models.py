from django.contrib.auth.models import AbstractUser
from django.db import models
from .managers import CustomUserManager

# Create your models here.

class CustomUser(AbstractUser):
    objects = CustomUserManager()

    def __str__(self):
        return self.username

