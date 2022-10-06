from django.contrib import admin
from django.urls import path
from .views import index, imagem


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('imagem/', imagem, name='imagem')
]

