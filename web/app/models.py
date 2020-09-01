from django.db import models
from django.contrib.auth.models import User
from mapbox_location_field.models import LocationField
import uuid

# Create your models here.

class Tag(models.Model):
    name = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.name

class Bench(models.Model):
    CATEGORY = (
        ('Picnic Bench', 'Picnic Bench'),
        ('Park Bench', 'Park Bench'),
        ('Picnicspot', 'Picnicspot'),
        ('Picnic Area', 'Picnic Area'),
    )

    CONDITION = (
        ('Spanking', 'Spanking'),
        ('Okay', 'Okay'),
        ('Apalling', 'Appalling'),
        ('Not There', 'Not There'),
    )

    CAPACITY = (
        ('1-2', '1-2'),
        ('3-5', '3-5'),
        ('6-10', '6-10'),
        ('10+', '10+'),
    )

    name = models.CharField(max_length=30, null=True)
    description = models.CharField(max_length=350, null=True, blank=True)
    # location = LocationField()
    image = models.ImageField(default="default.png", null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    category = models.CharField(max_length=30, null=True, choices=CATEGORY)
    condition = models.CharField(max_length=30, null=True, choices=CONDITION)
    tag = models.ManyToManyField(Tag, blank=True)
    capacity = models.CharField(max_length=30, null=True, choices=CAPACITY)

class Profile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    # username = User.get_username()
    name = models.CharField(max_length=50, null=True)
    website = models.URLField(null=True)
