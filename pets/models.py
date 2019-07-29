from django.conf import settings
from django.db import models
from django.utils import timezone
from gallery.models import Album
# from django.core.files.storage import FileSystemStorage

# fs = FileSystemStorage(location='/media/photos')

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
    name = models.CharField(max_length=200)
    pet_type = models.CharField(max_length=200)
    size = models.ForeignKey(Size, on_delete=models.CASCADE)
    gender = models.ForeignKey(Gender, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    album = models.ForeignKey(Album, on_delete=models.CASCADE, null=True, blank=True)
    city = models.CharField(max_length=1024)
    state = models.CharField(max_length=1024)
    neighborhood = models.CharField(max_length=1024)
    zipcode = models.CharField(max_length=12)
    description = models.TextField(null=True, blank=True)
    contact_name = models.CharField(max_length=100, null=True)
    phone_1 = models.CharField(max_length=12, blank=True)
    phone_2 = models.CharField(max_length=12, null=True, blank=True)
    email = models.CharField(max_length=200, null=True, blank=True)
    published_date = models.DateTimeField(blank=True, null=True)
    

    # def publish(self):
    #     self.published_date = timezone.now()
    #     self.save()

    def __str__(self):
        return self.name



    