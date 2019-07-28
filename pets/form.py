from django.forms import ModelForm
from .models import Pet

class PetForm(ModelForm):
    class Meta:
        model = Pet
        fields = [
            'name', 
            'pet_type', 
            'size', 
            'gender', 
            'category', 
            'city', 
            'state', 
            'neighborhood', 
            'zipcode', 
            'description',
            'contact_name',
            'phone_1',
            'phone_2',
            'email',
        ]