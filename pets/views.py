import json
from django.shortcuts import render
from django.http import HttpResponse
from django.forms.models import model_to_dict, modelform_factory
from django.http import JsonResponse
from .models import Pet, Size, Gender, Category
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

def size(request):
    all_objects = []
    for siz in Size.objects.all():
        _pet = model_to_dict(siz)
        all_objects.append(_pet)

    return JsonResponse(all_objects, safe=False)

def gender(request):
    all_objects = []
    for gen in Gender.objects.all():
        _pet = model_to_dict(gen)
        all_objects.append(_pet)

    return JsonResponse(all_objects, safe=False)   

def category(request):
    all_objects = []
    for cat in Category.objects.all():
        _pet = model_to_dict(cat)
        all_objects.append(_pet)

    return JsonResponse(all_objects, safe=False)

def new_pet(request):
    # Verifica se é uma requisição POST
    if request.method == 'POST':
        # Obtem o json do corpo da requisição
        data = json.loads(request.body)

        # Cria um formulário para o pet
        form = modelform_factory(Pet, fields=('name', 'category', 'size', 'gender', 'category'))
        # Popula os campos do formulário com os dados do json
        populated_form = form(data=data)

        # Valida o formulário
        if populated_form.is_valid():
            # Salva o registro na base de dados
            saved = populated_form.save()

            # Responde a requisição com os dados do pet recem cadastrado
            return JsonResponse(model_to_dict(saved), safe=False)

    # Caso contrário responde a requisição com erro
    return JsonResponse({'status': 'error'}, safe=False, status=400)
    

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