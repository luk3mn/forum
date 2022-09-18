from enum import auto
from tkinter import CASCADE
from tkinter.tix import AUTO
from django.db import models
from django.contrib.auth.models import User

class Publicacao(models.Model):
    titulo = models.CharField(max_length=150)
    duvida = models.CharField(max_length=450)
    data_publicacao = models.DateTimeField(auto_now=True)
    data_modificacao = models.DateField(auto_now=True)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, null=False)

    def __str__(self) -> str:
        return self.titulo

class Resposta(models.Model):
    respota = models.CharField(max_length=450)
    data_resposta = models.DateTimeField(auto_now=True)
    data_modificacao = models.DateTimeField(auto_now=True)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    # publicacao = models.ForeignKey(Publicacao, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.respota