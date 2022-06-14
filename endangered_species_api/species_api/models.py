from django.db import models

# Create your models here.

class Species(models.Model):
    commonName = models.CharField(max_length=32)
    species = models.CharField(max_length=64)
    order = models.CharField(max_length=32)
    suborder = models.CharField(max_length=32)
    habitat = models.CharField(max_length=64)
    diet = models.CharField(max_length=64)
    image = models.CharField(max_length=255)
    level = models.IntegerField()
