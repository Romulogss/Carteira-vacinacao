from pprint import pprint
from django.core.paginator import Paginator
from core.dao import (
    CriancaDAO,
    VacinaDAO,
    VacinacaoDAO
)
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
    return render(request, 'crianca/crianca.html', {'form': crianca})

def update(request, id):
    pass

def index(request):
    return render(request, 'crianca/index.html', {'obj': CriancaDAO.find_all()})

def crianca(request, id):
    result =  CriancaDAO.find_one(id)
    return render(
        request,
        'crianca/detail.html',
        {'crianca': result}
        )

def delete_crianca(request, id):
    result = CriancaDAO.delete(id)
    return redirect('index')

def vacinacao_index(request, id):
    crianca = CriancaDAO.find_one(id)
    form = VacinacaoForm(request.POST or None)
    vacinas = VacinaDAO.find_all()
    if form.is_valid():
        form.save()
        return redirect('vacinacao_index', id=id)
    lista_vacinacao = CriancaDAO.get_vacincas(id)
    paginator = Paginator(lista_vacinacao, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(
        request,
        'vacinacao/index.html',
        {
            'page_obj': page_obj,
            'form': form,
            'crianca': crianca,
            'vacinas': vacinas
        }
        )
