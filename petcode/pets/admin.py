from django.contrib import admin
from .models import Pet, PetType, Size, Gender, CategoryStatus, Category, CategoryAdmin

admin.site.register(Pet)
admin.site.register(PetType)
admin.site.register(Size)
admin.site.register(Gender)
admin.site.register(Category, CategoryAdmin)
admin.site.register(CategoryStatus)
