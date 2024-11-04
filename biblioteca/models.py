from django.db import models
from django.core.exceptions import ValidationError

class Autor(models.Model):
    nome = models.CharField(max_length=100)

def __str__(self):  
    return self.nome 

class Livro(models.Model):
    titulo = models.CharField(max_length=200)
    autor = models.ForeignKey(Autor, related_name='livros', on_delete=models.CASCADE)
    data_publicacao = models.DateField()
    numero_paginas = models.IntegerField()

def __str__(self): 
    return self.titulo 

class Livro(models.Model):

    def clean(self):
        if not self.autor:
            raise ValidationError("O livro deve ter um autor associado.")