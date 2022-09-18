from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import auth, messages
from django.contrib.auth.models import User
from django.contrib.messages import constants

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

        # testa se as senhas cadastradas coincidem
        if not senha == confirme_senha:
            messages.add_message(request, constants.ERROR, 'Senhas não coincidem!')
            return redirect('/autenticacao/cadastro')
        
        # testa campos em brancos
        if not (nome and sobrenome and usuario and senha and confirme_senha):
            messages.add_message(request, constants.ERROR, 'Preencha todos os campos obrigatórios')
            return redirect('/autenticacao/cadastro')
        
        # teste se o nome de usuario ja existe no banco de dados
        if User.objects.filter(username=usuario):
            messages.add_message(request, constants.ERROR, 'Usuario já existe')
            return redirect('/autenticacao/login/')
        try:
            user = User.objects.create_user(first_name=nome, last_name=sobrenome, username=usuario, password=senha) # instancia o novo usuario
            user.save() # persistir no db
            messages.add_message(request, constants.SUCCESS, 'Usuário cadastrado com sucesso')
            return redirect('/autenticacao/login/')
        except:
            messages.add_message(request, constants.ERROR, 'Erro interno do sistema!')
            return redirect('/autenticaco/cadastro/')
    elif request.method == "GET":
        if request.user.is_authenticated:
            return redirect('/')


    return render(request, 'autenticacao/signup.html')

def logout(request):
    auth.logout(request)
    return redirect('/')