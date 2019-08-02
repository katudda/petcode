import json
from django.shortcuts import render
from django.http import HttpResponse
from django.forms.models import model_to_dict 
from django.http import JsonResponse
from .models import Pet
from .form import PetForm


import datetime

def home(request):
    data = {}
    return render(request, 'pet/home.html', data)

def list_pet(request):
    all_objects = []
    for pet in Pet.objects.all():
        _pet = model_to_dict(pet)
        _pet['images'] = []
        _pet['category'] = model_to_dict(pet.category)
        _pet['gender'] = model_to_dict(pet.gender)
        _pet['size'] = model_to_dict(pet.size)

        if pet.album:
            if pet.album.images:
                images = [img for img in pet.album.images.all()]
                for image in images:
                    _pet['images'].append(image.data_thumbnail.url)
        del(_pet['album'])
        all_objects.append(_pet)

    return JsonResponse(all_objects, safe=False)


def new_pet(request):
    data = {}
    form = PetForm(request.POST or None)

    if form.is_valid():
        form.save()
        return list_pet(request)
    data['form'] = form
    return render(request, 'pet/form.html', data)

def update_pet(request, pk):
    pet = Pet.objects.get(pk=pk)
    form = PetForm(request.POST or None, instance=pet)
    data = {}
    if form.is_valid():
        form.save()
        return list_pet(request)
    data['form'] = form
    data['pet'] = pet
    return render(request, 'pet/form.html', data)

def delete_pet(request, pk):
    pet = Pet.objects.get(pk=pk)
    form = PetForm(request.POST or None, instance=pet)
    pet.delete()
    return list_pet(request)