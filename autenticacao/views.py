from django.shortcuts import render, redirect
from django.http import HttpResponse

def login(request):

    # se o botão for pressionado
    if request.method == 'POST':
        usuario = request.POST.get('usuario') 
        senha = request.POST.get('senha')

        return HttpResponse(usuario)
    return render(request, 'autenticacao/signin.html')

def cadastro(request):
    return render(request, 'autenticacao/signup.html')