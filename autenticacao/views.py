from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import auth
from django.contrib.auth.models import User

def login(request):

    # se o botão for pressionado
    if request.method == 'POST':
        usuario = request.POST.get('usuario') 
        senha = request.POST.get('senha')

        # prepara o usuario e senha para o login
        usuario_logado = auth.authenticate(username=usuario, password=senha)

        if usuario_logado: # verifica se usuario e senha existem
            auth.login(request, usuario_logado) # realiza o login
            return redirect('/')
        else: # caso não encontre o usuário e a senha informados
            return HttpResponse("Usuário e/ou senha incorretos")
    elif request.method == "GET": # impedi que o usuário logado redirecione para a pagina de login/cadastro
        if request.user.is_authenticated:
            return redirect('/')
    
    return render(request, 'autenticacao/signin.html')

def cadastro(request):

    if request.method == "POST":

        # coleta dos dados
        nome = request.POST.get('nome')
        sobrenome = request.POST.get('sobrenome')
        usuario = request.POST.get('usuario')
        senha = request.POST.get('senha')
        confirme_senha = request.POST.get('confirme-senha')

        if not senha == confirme_senha:
            # return redirect('/autenticacao/cadastro')
            return HttpResponse('Senhas não coincidem!')
        
        if not (nome and sobrenome and usuario and senha and confirme_senha):
            return redirect('/autenticacao/cadastro')
        
        if User.objects.filter(username=usuario):
            return HttpResponse("Usuario já existe")
            

        return HttpResponse([nome, sobrenome, usuario, senha])
    elif request.method == "GET":
        if request.user.is_authenticated:
            return redirect('/')


    return render(request, 'autenticacao/signup.html')

def logout(request):
    auth.logout(request)
    return redirect('/')