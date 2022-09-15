from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login, name='autenticacao.login'),
    path('cadastro/', views.cadastro, name='autenticacao.cadastro'),
]