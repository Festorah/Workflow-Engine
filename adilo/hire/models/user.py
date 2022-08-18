from django.contrib.auth.models import AbstractUser
from django.db import models
import uuid


class User(AbstractUser):
    name = models.CharField(
        max_length=50,
        null=True,
        blank=True,
        unique=True,
    )

