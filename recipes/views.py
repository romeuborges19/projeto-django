from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'recipes/pages/home.html')

def my_view(request):
    return HttpResponse("TESTE 1")

def tela_login(request):
    return HttpResponse("TELA DE LOGIN")

def register_page(request):
    return HttpResponse("TELA DE CADASTRO")

def main_page(request):
    return render(request, 'recipes/pages/main-page.html')
