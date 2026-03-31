from django.urls import path
from . import views

urlpatterns = [
    path('livros/', views.listar_livros),
    path('lidos/', views.livros_lidos),
]