from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='publicacao.home'),
    path('publicacao/', views.pub, name='publicacao.pub'),
]