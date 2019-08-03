from django.shortcuts import render
from django.http import HttpResponse
from .models import User
from .form import UserForm
# from django.urls import reverse_lazy

import datetime

def home(request):
    data = {}
    return render(request, 'users/home.html', data)

def list_user(request):
    data = {}
    data['user'] = User.objects.all()
    return render(request,'users/list_user.html', data)   

def new_user(request):
    data = {}
    form = UserForm(request.POST or None)

    if form.is_valid():
        form.save()
        return list_user(request)
    data['form'] = form
    return render(request, 'users/form.html', data)