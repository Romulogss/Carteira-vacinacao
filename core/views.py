from core.dao import CriancaDAO
from django.shortcuts import redirect, render
from .forms import (
    CriancaForm,
    VacinaForm,
    VacinacaoForm,
)
# Create your views here.
def create(request):
    crianca = CriancaForm(request.POST or None)
    if crianca.is_valid():
        crianca.save()
        return redirect('index')
    return render(request, 'crianca.html', {'form': crianca})
    

def index(request):
    return render(request, 'index.html', {'obj': CriancaDAO.findAll()})


def crianca(request, id):
    result =  CriancaDAO.findOne(id)
    vacinas = CriancaDAO.getVacincas(id)

    return render(
        request,
        'detail.html',
        {'crianca': result,
        'vacinas': vacinas}
        )
