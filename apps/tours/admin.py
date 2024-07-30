from django.contrib import admin
from apps.tours.models import Category, Country, Tour


admin.site.register(Category)
admin.site.register(Country)
admin.site.register(Tour)
