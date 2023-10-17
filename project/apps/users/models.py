from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class User(AbstractUser):
    bio = models.TextField(blank=True)
    avatar = models.ImageField(upload_to="users_avatars", blank=True)
    address = models.CharField(max_length=250, blank=True)
    telegram = models.CharField(max_length=250, blank=True)
    instagram = models.CharField(max_length=250, blank=True)
