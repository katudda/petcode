from django.shortcuts import render
from django.http import HttpResponse
from .models import Pet
from .form import PetForm


import datetime

def home(request):
    data = {}
    return render(request, 'pet/home.html', data)

def list_pet(request):
    data = {}
    data['pets'] = Pet.objects.all()
    return render(request,'pet/list_pet.html', data)   

def new_pet(request):
    data = {}
    form = PetForm(request.POST or None)

    if form.is_valid():
        form.save()
        return list_pet(request)
    data['form'] = form
    return render(request, 'pet/form.html', data)

