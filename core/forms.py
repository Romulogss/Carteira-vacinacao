from django import forms
from django.db.models import fields
from .models import (
    Crianca,
    Vacina,
    Vacinacao,
)

class CriancaForm(forms.ModelForm):
    class Meta:
        model = Crianca
        fields = '__all__'

class VacinaForm(forms.ModelForm):
    class Meta:
        model = Vacina
        fields = '__all__'

class VacinacaoForm(forms.ModelForm):
    class Meta:
        model = Vacinacao
        fields = '__all__'