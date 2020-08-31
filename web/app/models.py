from django.db import models
from mapbox_location_field.models import LocationField

# Create your models here.

class Bench(models.Model):
    name = models.CharField(max_length=30, null=True)
    location = LocationField()
    image = models.ImageField(default="", null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)