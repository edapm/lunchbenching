from django.contrib import admin

# Register your models here.

from . models import *

class ProfileAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}

class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'body', 'bench', 'created_on')
    search_fields = ('name', 'body')

admin.site.register(Bench)
admin.site.register(Profile, ProfileAdmin)
admin.site.register(Comments, CommentAdmin)

