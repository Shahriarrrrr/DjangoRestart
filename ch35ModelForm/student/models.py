from django.db import models

# Create your models here.

class Profile(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    password = models.CharField(max_length=255)
    phone = models.IntegerField(max_length=20, blank=True)