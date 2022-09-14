from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Dashboard(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    temperatura = models.CharField(max_length=10, default=0)
    umidade = models.CharField(max_length=10, blank=False, default=0)
    tempo = models.CharField(max_length=100, default=0.00)
    power = models.BooleanField(default=False)
