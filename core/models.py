from django.db import models

# Create your models here.
class Crianca(models.Model):
    nome = models.CharField(
        max_length=50
        )
    cpf = models.CharField(
        max_length=11,
        unique=True
        )

    def __str__(self):
        return self.nome

class Vacina(models.Model):
    nome = models.CharField(
        max_length=50
        )
    descricao = models.TextField()
    fabricante = models.CharField(
        max_length=20
        )

    def __str__(self):
        return f'{self.nome} | {self.fabricante}'

class Vacinacao(models.Model):
    lote = models.CharField(
        max_length=20
        )
    data = models.DateField()
    crianca = models.ForeignKey(
        Crianca,
        on_delete=models.CASCADE
        )
    vacina = models.ForeignKey(
        Vacina,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return f'{self.crianca.nome} | {self.data}'