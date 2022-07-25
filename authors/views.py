from django.http import Http404
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm

from authors.forms import CreateUserForm

# Create your views here.

def register_view(request):
    register_form_data = request.session.get('register_form_data', None)
    form = CreateUserForm(register_form_data)

    context = {'form': form}
    return render(request, 'authors/pages/register_view.html', context)

def register_create(request):
    if not request.POST:
        raise Http404()

    POST = request.POST
    request.session['register_form_data'] = POST
    form = CreateUserForm(POST)

    if form.is_valid():
        form.save()

        del(request.session['register_form_data'])

    return redirect('authors:register')
