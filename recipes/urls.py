from django.contrib import admin
from django.urls import include, path

from recipes.views import home, my_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home)
]
