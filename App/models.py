from django.db import models

class Plataforma(models.Model):
    nome = models.CharField(
        max_length = 100
    )
    link = models.CharField(
        max_length = 100)


class Ferramenta(models.Model):
    nome = models.CharField(
        max_length = 100
    )
    link = models.CharField(
        max_length = 100)
