from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Secador(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    nome = models.CharField(max_length=200)
    modelo = models.CharField(max_length=200)
    localizacao = models.CharField(max_length=200)