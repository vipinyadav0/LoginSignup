from django.forms import ModelForm
from django import forms

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CreateUserForms(UserCreationForm):
    
    username = forms.CharField(max_length=101)
    email = forms.EmailField()
    remember_me = forms.BooleanField(required=False)
    
    class Meta:
        model = User
        
        fields = ['username', 'email', 'password1', 'password2']
    