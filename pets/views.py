import json
from django.shortcuts import render
from django.http import HttpResponse
from django.forms.models import model_to_dict, modelform_factory
from django.http import JsonResponse
from .models import Pet, Size, Gender, Category
from gallery.models import Album, Image
from gallery.forms import ImageCreateForm
from .form import PetForm
from users.models import User


import datetime

def home(request):
    data = {}
    return render(request, 'pet/home.html', data)

def list_pet(request):
    all_objects = []
    model = Pet.objects
    # Obtem todas as chaves do GET
    for k,vals in request.GET.lists():
        # Obtem todos os valores da chave
        for v in vals:
            
            # Busca por conteudo incompleto
            if k in ['name', 'pet_type']:
                model = model.filter(**{"%s__icontains" % k: v})
            
            # Busca por valor exato
            else:
                model = model.filter(**{k: v})
        
    for pet in model.all():
        _pet = model_to_dict(pet)
        _pet['images'] = []
        _pet['user'] = model_to_dict(pet.user)
        _pet['category'] = model_to_dict(pet.category)
        _pet['gender'] = model_to_dict(pet.gender)
        _pet['size'] = model_to_dict(pet.size)
        _pet['published_date'] = pet.published_date

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

        # TODO: Verificar se o usuario existe
        user = User.objects.get(pk=int(data['user']))
        data['user'] = user.id

        album = Album.objects.create(title="name")
        data['album'] = album.id
        # Cria um formulário para o pet
        form = modelform_factory(Pet, fields=(
            'user', 
            'name', 
            'pet_type', 
            'size', 
            'gender',  
            'category', 
            'album' , 
            'city', 
            'state',
            'neighborhood',
            'description',
            'contact_name',
            'phone_1',
            'phone_2',
            'email'
            ))
        # Popula os campos do formulário com os dados do json
        populated_form = form(data=data)

        # Valida o formulário
        if populated_form.is_valid():
            # Salva o registro na base de dados
            pet = saved = populated_form.save()

            # Responde a requisição com os dados do pet recem cadastrado
            return JsonResponse(model_to_dict(saved), safe=False)
        else:
            return JsonResponse({'status': 'error', 'message': populated_form.errors}, safe=False, status=400)

    # Caso contrário responde a requisição com erro
    return JsonResponse({'status': 'error'}, safe=False, status=400)
    

def update_pet(request, pk):
    # Verifica se é uma requisição POST
    if request.method == 'PATCH':
        pet = Pet.objects.get(pk=pk)
        # Obtem o json do corpo da requisição e atualiza o dict do pet
        update_data = {**model_to_dict(pet), **json.loads(request.body)}
        form = PetForm(update_data or None, instance=pet)
        if form.is_valid():
            updated = form.save()
            return JsonResponse(model_to_dict(updated), safe=False)
        else:
            return JsonResponse({'status': 'error', 'message': form.errors}, safe=False, status=400)

    
    # Caso contrário responde a requisição com erro
    return JsonResponse({'status': 'error'}, safe=False, status=400)
    
def upload_pet_image(request, pk):
    if request.method == 'POST':
        # Pega o Pet
        pet = Pet.objects.get(pk=pk)
        total_images = pet.album.images.count()
        limit = 5
        if total_images >= limit:
            return JsonResponse({
                'status': 'error', 
                'message': f'You cant upload more than {limit} images.'
            }, safe=False, status=204)

        # Pega a imagem do request e cria na base de dados
        image = Image.objects.create(data=request.FILES['data'])

        # Relaciona a imagem a um album
        image.image_albums.add(pet.album.id)

        # Responde a requisição
        return JsonResponse({'status': 'success', 'url': image.data_thumbnail.url}, safe=False)

    # Informa que o metodo é inválido
    return JsonResponse({'status': 'error'}, safe=False, status=405)

def delete_pet(request, pk):
    pet = Pet.objects.get(pk=pk)
    form = PetForm(request.POST or None, instance=pet)
    pet.delete()
    return list_pet(request)