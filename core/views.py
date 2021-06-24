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
def ciranca_create(request):
    crianca = CriancaForm(request.POST or None)
    if crianca.is_valid():
        crianca.save()
        return redirect('index')
    return render(request, 'crianca/form.html', {'form': crianca})

def crianca_update(request, id):
    crianca = CriancaDAO.find_one(id)
    form = CriancaForm(request.POST or None, instance=crianca)
    if form.is_valid():
        form.save()
        return redirect('index')
    return render(request, 'crianca/form.html', {'crianca': crianca})

def crianca_index(request):
    lista_criancas = CriancaDAO.find_all()
    return render(request, 'crianca/index.html', {'lista_criancas': lista_criancas })

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

def vacinacao_delete(request, id):
    vacinacao = VacinacaoDAO.find_one(id)
    if request.method == 'POST':
        id_crianca = vacinacao.crianca.id
        VacinacaoDAO.delete(vacinacao.id)
        return redirect('vacinacao_index', id=id_crianca)