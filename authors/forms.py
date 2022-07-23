from django.forms import EmailInput, ModelForm, PasswordInput, TextInput
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User

        fields = [
            'first_name', 
            'last_name', 
            'username',  
            'email',  
            'password1',  
            'password2'
        ]

    

        widgets = {
            'first_name':TextInput(attrs={
                'class':"form-control",
                'style': 'width: 190px; height: 30px; padding-left:5px',
            }),
            'last_name':TextInput(attrs={
                'class':"form-control",
                'style': 'width: 190px; height: 30px; padding-left:5px',
            }),
            'username':TextInput(attrs={
                'class':"form-control",
                'style': 'width: 420px; height: 30px; padding-left:10px'
            }),
            'email':EmailInput(attrs={
                'class':"form-control",
                'style': 'width: 420px; height: 30px; padding-left:10px'
            }),
        }
