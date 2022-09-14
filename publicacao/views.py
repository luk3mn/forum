from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from publicacao.models import Publicacao
from django.contrib.auth.models import User

def home(request):
    publicacao = Publicacao.objects.all()
    return render(request, 'publicacao/home.html', {'publicacao':publicacao})

def publicacao(request, id_pub):
    publicacao = Publicacao.objects.get(id=id_pub)
    return render(request, 'publicacao/publicacao.html', {'publicacao':publicacao})

def publicar(request):
    usuario = request.user # pega o usuário logado
    publicacao = Publicacao.objects.filter(usuario=usuario)
    # id_usuario = request.user.id # pega o 'id' do usuário logado
    # usuario = get_object_or_404(User, id=id_usuario) # 
    if request.method == "POST":
        titulo = request.POST.get('titulo') # pega o campo 'titulo' do form
        duvida = request.POST.get('duvida') # pega o campo 'duvida' do form

        add_duvida = Publicacao(usuario=usuario, titulo=titulo, duvida=duvida) # add no DB
        add_duvida.save() # salva no DB

        # return redirect(f'/publicacao/{id_usuario}')

    return render(request, 'publicacao/publicar.html',{'publicacao':publicacao})