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
