from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, 'publicacao/home.html')

def pub(request):
    return render(request, 'publicacao/publicacao.html')