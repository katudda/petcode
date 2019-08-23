from django.contrib import admin
from .models import Pet, PetType, CategoryStatus, Category, Image

admin.site.register(Pet)
admin.site.register(Image)
admin.site.register(PetType)
admin.site.register(Category)
admin.site.register(CategoryStatus)
