from django.db import models


class Alunos(models.Model):

    cpf = models.CharField(max_length=14, null=False, blank=False)
    sexo = models.CharField(max_length=20, default="Masculino")
    nome = models.CharField(max_length=200, null=False, blank=False)
    telefone = models.CharField(max_length=14, null=False, blank=False)
    dt_nasc = models.CharField(max_length=20)

    
    def __str__(self):
        return self.nome