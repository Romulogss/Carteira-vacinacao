from .models import (
    Crianca,
    Vacina,
    Vacinacao,
)
from pprint import pprint

class CriancaDAO:
    manager = Crianca.objects

    @staticmethod
    def findAll():
        criancas = __class__.manager.all()
        return criancas

    @staticmethod
    def findOne(id):
        crianca = __class__.manager.get(pk=id)
        return crianca

    @staticmethod
    def getVacincas(id):
        crianca = __class__.findOne(id)
        vacinas = crianca.vacinacao_set.all()
        return vacinas