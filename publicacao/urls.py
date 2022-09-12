from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='publicacao.home'),
    path('publicacao/', views.publicacao, name='publicacao.publicacao'),
    path('publicar/', views.publicar, name='publicacao.publicar')
]