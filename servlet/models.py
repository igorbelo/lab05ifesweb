from __future__ import unicode_literals

from django.db import models

class Pessoa(models.Model):
    nome = models.CharField(max_length=200)
    email = models.CharField(max_length=60)
    idade = models.IntegerField()

    def __str__(self):
        return self.nome
