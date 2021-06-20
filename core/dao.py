from django.shortcuts import get_list_or_404, get_object_or_404
from .models import (
    Crianca,
    Vacina,
    Vacinacao,
)
from pprint import pprint

class CriancaDAO:
    manager = Crianca.objects

    @staticmethod
    def find_all():
        criancas = __class__.manager.all()
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
    def delete(id) -> str :
        crianca = __class__.findOne(id)
        nome = crianca.nome
        crianca.delete()
        return f'{nome} foi deletada com sucesso!'


class VacinacaoDAO:
    manager = Vacinacao.objects
    @staticmethod
    def find_all():
        vacinacao = __class__.manager.all()
        return vacinacao


class VacinaDAO:
    manager = Vacina.objects

    @staticmethod
    def find_all():
        vacinas = get_list_or_404(Vacina)
        return vacinas