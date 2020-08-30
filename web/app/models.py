from django.db import models

# Create your models here.

class Bench(models.Model):
    name = models.CharField(max_length=30, null=True)
    location = models.CharField
