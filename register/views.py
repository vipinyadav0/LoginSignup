from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth import authenticate, login, logout # importing login logout

from django.contrib import messages

from django.conf import Settings, settings

# from Authentication import settings
# from django.core.mail import send_mail
# from django.contrib.sites.shortcuts import get_current_site

from django.contrib.auth.decorators import login_required

from .models import *
from .forms import CreateUserForms

def logout_view(request):
    logout(request)
    return redirect('login')


def login_page(request):
    
    request_data = request.POST
    # print(request_data)
    
    if request.method == 'POST':
        username = request_data.get('username')
        password = request_data.get('password')

        user = authenticate(request, username= username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'Username or Password is incorrect')
    
    return render(request, 'register/login.html')

def signup_page(request):
    # if request.user.is_authenticated:
    #     return render(request, 'home')
    # else:
    
    request_data = request.POST
    # print(request_data)
    # print(request.method)
        
    if request.method == 'POST':

        form = CreateUserForms(request_data)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
                
            messages.success(request, "Account was created for " + user)
                
            return redirect('login')
    else:
        form = CreateUserForms()
            
    context = {'form' : form}
    return render(request, 'register/signup.html', context)



@login_required(login_url='login')
def home_page(request):
    return render(request, 'register/home.html')