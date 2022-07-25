from django.forms import EmailInput, ModelForm, PasswordInput, TextInput
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from django.core.exceptions import ValidationError
from django.contrib import messages
import re

def strong_password(password1):
    regex = re.compile(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9]).{8,}$')

    if not regex.match(password1):
        raise ValidationError(
            'Sua senha deve conter pelo menos 1 letra minúscula, 1 letra maíuscula, um número e ter mais que 8 caracteres.', code='invalid'
        )

class CreateUserForm(UserCreationForm):

    first_name=forms.CharField(
        error_messages={'required':'Insira seu primeiro nome.'},
        label='First name'
    )

    last_name=forms.CharField(
        error_messages={'required':'Insira seu último nome.'},
        label='Last name'
    )

    username=forms.CharField(
        error_messages={
            'required':'Insira um nome de usuário.',
            'max_length': 'O nome de usuário deve ter menos do que 50 caracteres',
            'min_length': 'O nome de usuário deve ter mais do que 4 caracteres'}
            max_length=50,
            min_length=4
    )
        

    email=forms.CharField(
        error_messages={'required':'Insira seu e-mail.'}
        label='E-mail'

    )


    password1=forms.CharField(
        required=True,
        widget=forms.PasswordInput(),
        validators=[strong_password],
        error_messages={'required':'Este campo é obrigatório'},
        label='password1'
    )

    password2=forms.CharField(
        required=True,
        widget=forms.PasswordInput(),
        error_messages={'required':'Este campo é obrigatório'},
        label='password2'
    )

    username
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

