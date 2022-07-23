from django.contrib import admin
from django.urls import include, path

from recipes.views import home, main_page, tela_login

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home),
    path('login/', tela_login),
    path('main/', main_page)
]
