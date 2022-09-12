from django.shortcuts import render
from django.http import HttpResponse
from publicacao.models import Publicacao

def home(request):
    publicacao = Publicacao.objects.all()
    return render(request, 'publicacao/home.html', {'publicacao':publicacao})

def publicacao(request):
    return render(request, 'publicacao/publicacao.html')

def publicar(request):
    return render(request, 'publicacao/publicar.html')