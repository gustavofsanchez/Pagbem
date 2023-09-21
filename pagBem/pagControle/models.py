from django.db import models


class Plano(models.Model):
    nome = models.CharField(max_length=100)
    valor = models.FloatField()
    duracaoDias = models.IntegerField()
    frequencia = models.IntegerField()
    
    def __str__(self):
        return self.nome

class Cliente(models.Model):
    nome = models.CharField(max_length=100)
    login = models.CharField(max_length=20)
    senha = models.CharField(max_length=20)
    ativo = models.BooleanField()
    ingresso = models.DateTimeField(auto_now_add=True)
    atualizadoEm = models.DateTimeField(auto_now=True)
    vencimento = models.DateField()
    plano = models.ForeignKey(Plano, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.nome

    