from django.contrib import admin
from mapbox_location_field.admin import MapAdmin

# Register your models here.

from . models import *

class ProfileAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}

admin.site.register(Bench, MapAdmin)
admin.site.register(Profile, ProfileAdmin)

