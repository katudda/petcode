from django.contrib import admin
from .models import Pet
from .models import Size
from .models import Gender
from .models import Category
from .models import CategoryStatus


# Register your models here.
admin.site.register(Pet)
admin.site.register(Size)
admin.site.register(Gender)
admin.site.register(Category)
admin.site.register(CategoryStatus)
