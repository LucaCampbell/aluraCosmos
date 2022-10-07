from django.urls import path
from .views import index, imagem
from django.urls import path

from .views import index, imagem

urlpatterns = [
    path('', index, name='index'),
    path('<int:foto_id>', imagem, name='imagem')
]

