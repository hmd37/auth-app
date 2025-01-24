from django.contrib.auth.models import AbstractUser
from django.utils.timezone import now
from django.db import models


class CustomUser(AbstractUser):
    username = models.CharField(max_length=255, unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)

    is_active = models.BooleanField(default=True)

    date_joined = models.DateTimeField(default=now)

    def __str__(self):
        return self.username
