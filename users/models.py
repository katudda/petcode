from django.db import models
 

class User(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(max_length=254, blank=True, null= True, unique= True)
    born_date = models.DateField()
    
    def __str__(self):
        return self.first_name + ' ' + self.last_name
