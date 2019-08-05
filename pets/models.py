from django.conf import settings
from django.db import models
from django.utils import timezone
from gallery.models import Album
from users.models import User


class Size(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name

class Gender(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=100)
    
    class Meta:
        verbose_name_plural = 'Categories'
    
    def __str__(self):
        return self.name     

class Pet(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=200, null=False)
    description = models.TextField(null=True, blank=True)
    pet_type = models.CharField(max_length=200, null=False)
    size = models.ForeignKey(Size, on_delete=models.CASCADE, null=False)
    gender = models.ForeignKey(Gender, on_delete=models.CASCADE, null=False)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=False)
    state = models.CharField(max_length=1024, null=False)
    city = models.CharField(max_length=1024, null=False)
    contact_name = models.CharField(max_length=100, null=False)
    phone_1 = models.CharField(max_length=12, null=True, blank=True)
    phone_2 = models.CharField(max_length=12, null=True, blank=True)
    email = models.CharField(max_length=200, null=True, blank=True)
    album = models.ForeignKey(Album, on_delete=models.CASCADE, null=True, blank=True)
    published_date = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return self.name



    