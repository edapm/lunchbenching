from django.contrib import admin

# Register your models here.

from . models import *

class ProfileAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}

admin.site.register(Bench)
admin.site.register(Profile, ProfileAdmin)

