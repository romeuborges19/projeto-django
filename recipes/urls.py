from django.contrib import admin
from django.urls import include, path

from recipes.views import home, my_view, register_page, tela_login

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home),
    path('login/', tela_login),
    path('register/', register_page)
]
