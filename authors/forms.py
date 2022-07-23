from django.forms import EmailInput, ModelForm, PasswordInput, TextInput
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from django.core.exceptions import ValidationError
from django.contrib import messages


class CreateUserForm(UserCreationForm):

    def clean_first_name(self):
        data = self.cleaned_data.get('first_name')

        if 'Romeu' in data:
            raise forms.ValidationError(
                'Não é permitido Romeu', 
                code='invalid')

        return data

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

