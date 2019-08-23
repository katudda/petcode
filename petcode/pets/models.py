from django.conf import settings
from django import forms
from django.contrib import admin
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFit
from .constants import SIZE, GENDER 

class PetType(models.Model):
    name = models.CharField(max_length=100, unique=True)
    
    def __str__(self):
        return self.name
        
class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    
    class Meta:
        verbose_name_plural = 'Categories'
    
    def __str__(self):
        return self.name       

class CategoryStatus(models.Model):
    name = models.CharField(max_length=100, unique=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True)

    class Meta:
        verbose_name_plural = 'Category Status'
    
    def __str__(self):
        return self.name 
        

class Image(models.Model):
    image = models.ImageField(upload_to='images', blank=True)
    data_thumbnail = ImageSpecField(source='image',
                                    processors=[ResizeToFit(
                                        height=200)],
                                    format='JPEG',
                                    options={'quality': 80})


class Pet(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    images = models.ManyToManyField(Image, blank=True)
    name = models.CharField(max_length=200, null=False)
    description = models.TextField(null=True, blank=True)
    pet_type = models.ForeignKey(PetType, on_delete=models.CASCADE, null=False)
    size = models.CharField(
        max_length=100,
        choices=SIZE,
        blank=True,
        null=True
    )
    gender = models.CharField(
        max_length=100,
        choices=GENDER,
        blank=True,
        null=True
    )
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=False, related_name='category')
    category_status = models.ForeignKey(CategoryStatus, on_delete=models.CASCADE, null=True, blank=True, related_name='category_status')
    state = models.CharField(max_length=1024, null=False)
    city = models.CharField(max_length=1024, null=False)
    contact_name = models.CharField(max_length=100, null=False)
    phone_1 = models.CharField(max_length=12, null=True, blank=True)
    phone_2 = models.CharField(max_length=12, null=True, blank=True)
    email = models.CharField(max_length=200, null=True, blank=True)
    published_date = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return self.name