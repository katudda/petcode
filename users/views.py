import json
from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from django.http import JsonResponse
from django import forms
from .forms import UserRegistrationForm
from django.views.decorators.csrf import csrf_exempt

def home(request):
    return render(request, 'users/home.html')

@csrf_exempt
def new_user(request):
    if request.method == 'POST':
        body = json.loads(request.body)
        form = UserRegistrationForm(body)
        try:
            form.is_valid()
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
                # user = authenticate(username = username, password = password2)
                # login(request, user)
                return JsonResponse({'success': True, 'message': 'Cadastro realizado com sucesso'})    
            else:
                return JsonResponse({'success': False, 'message': 'Username ou e-mail já estão sendo usados.'})
        except:
            print(form.errors)
            return JsonResponse({'success': False, 'message': 'Cadastro inválido'})

    # TODO rever esse fluxo quando o metodo nao for POST        
    else:
        form = UserRegistrationForm()
        
    return render(request, 'users/form.html', {'form' : form})

@csrf_exempt
def auth_login(request):
    if request.method == 'POST':
        body = json.loads(request.body)

        # TODO check if user is authenticated
        # if request.user.is_authenticated():
        #     return JsonResponse({'success': True, 'message': 'Usuário já logado'})
        # else:

        username = body.get('username')
        password = body.get('password')
        user = authenticate(request, username=username, password=password)    
        if user is not None:
            login(request, user)
            return JsonResponse({'success': True, 'message': 'Usuário logado com sucesso'})
        else:
            return JsonResponse({'success': False, 'message': 'Tente novamente'})
    
    else:
        return JsonResponse({'success': False, 'message': 'Should use the verb POST for your resquest'})
