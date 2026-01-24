from django.contrib import admin
from django.contrib.admin import ModelAdmin

from pets.models import Pet


# Register your models here.
@admin.register(Pet)
class PetAdmin(ModelAdmin):
    list_display = ['name', 'slug']