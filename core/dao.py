from django.shortcuts import get_object_or_404
from .models import (
    Crianca,
    Vacina,
    Vacinacao,
)

class CriancaDAO:
    manager = Crianca.objects

    @staticmethod
    def find_all():
        criancas = __class__.manager.order_by('-id').all()
        return criancas

    @staticmethod
    def find_one(id):
        crianca = get_object_or_404(Crianca, pk=id)
        return crianca

    @staticmethod
    def get_vacincas(id):
        crianca = __class__.find_one(id)
        vacinas = crianca.vacinacao_set.order_by('-data').all()
        return vacinas

    @staticmethod
    def delete(id):
        crianca = __class__.find_one(id)
        crianca.delete()

class VacinaDAO:
    manager = Vacina.objects

    @staticmethod
    def find_all():
        vacinas = __class__.manager.all()
        return vacinas

    @staticmethod
    def find_one(id):
        vacina = get_object_or_404(Vacina, pk=id)
        return vacina

    @staticmethod
    def delete(id):
        vacina = __class__.find_one(id)
        vacina.delete()

class VacinacaoDAO:
    manager = Vacinacao.objects

    @staticmethod
    def find_all():
        vacinacao = __class__.manager.all()
        return vacinacao
    
    @staticmethod
    def find_one(id):
        vacinacao = get_object_or_404(Vacinacao, pk=id)
        return vacinacao

    @staticmethod
    def delete(id):
        vacinacao = get_object_or_404(Vacinacao, pk=id)
        vacinacao.delete()
