from datetime import datetime

from django.db import models


class Usuario(models.Model):
    nome = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    def __str__(self):
        return self.nome


class Fotografia(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    imagem = models.ImageField(upload_to='fotos/%d/%m/%Y/')
    nome_foto = models.CharField(max_length=200)
    descricao = models.TextField()
    data_publicacao = models.DateTimeField(default=datetime.now, blank=True)
    categoria = models.CharField(max_length=100)
    publicada = models.BooleanField(default=False)
