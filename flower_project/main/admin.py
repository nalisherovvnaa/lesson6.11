from django.contrib import admin
from .models import Flower

@admin.register(Flower)
class FlowerAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'available']
    search_fields = ['name']
    list_filter = ['available']
