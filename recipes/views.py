from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm

from authors.forms import CreateUserForm

# Create your views here.

def home(request):
    return render(request, 'recipes/pages/home.html')


def tela_login(request):
    return HttpResponse("TELA DE LOGIN")

def main_page(request):
    return render(request, 'recipes/pages/main-page.html')
