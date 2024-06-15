from django.db import models
from django.contrib.auth.models import User

class Plataforma(models.Model):
    nome = models.CharField(
        max_length = 100
    )
    link = models.CharField(
        max_length = 100)
    usuarios = models.ManyToManyField(User, related_name='plataformas')

    def __str__(self):
        return self.nome


class Ferramenta(models.Model):
    nome = models.CharField(
        max_length = 100
    )
    link = models.CharField(
        max_length = 100)
