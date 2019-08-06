from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from django import forms
from .forms import UserRegistrationForm

def home(request):
    return render(request, 'users/home.html')
    
def new_user(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            userObj = form.cleaned_data
            username = userObj['username']
            email =  userObj['email']
            password1 =  userObj['password1']
            password2 = userObj['password2']
            first_name = userObj['first_name']
            last_name = userObj['last_name']
            if not (User.objects.filter(username=username).exists() or User.objects.filter(email=email).exists()):
                # Check that the two password entries match
                if password1 and password2 and password1 != password2:
                    raise forms.ValidationError("Passwords don't match")
                User.objects.create_user(username, email, password=password2, first_name=first_name, last_name=last_name)
                user = authenticate(username = username, password = password2)
                login(request, user)
                return HttpResponseRedirect('/users')    
            else:
                raise forms.ValidationError('Looks like a username with that email or password already exists')
                
    else:
        form = UserRegistrationForm()
        
    return render(request, 'users/form.html', {'form' : form})