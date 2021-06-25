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
def crianca_index(request):
    lista_criancas = CriancaDAO.find_all()
    paginator = Paginator(lista_criancas, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    lista_criancas = page_obj.object_list
    return render(
        request,
        'crianca/index.html',
        {
            'lista_criancas': lista_criancas,
            'paginator': page_obj
        })

def crianca_create(request):
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


def crianca(request, id):
    result =  CriancaDAO.find_one(id)
    return render(
        request,
        'crianca/detail.html',
        {'crianca': result}
        )

def delete_crianca(request, id):
    if request.method == "POST":
        CriancaDAO.delete(id)
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
    lista_vacinacao = page_obj.object_list
    return render(
        request,
        'vacinacao/index.html',
        {
            'paginator': page_obj,
            'form': form,
            'crianca': crianca,
            'vacinas': vacinas,
            'lista_vacinacao': lista_vacinacao
        }
        )

def vacinacao_delete(request, id):
    vacinacao = VacinacaoDAO.find_one(id)
    if request.method == 'POST':
        id_crianca = vacinacao.crianca.id
        VacinacaoDAO.delete(vacinacao.id)
        return redirect('vacinacao_index', id=id_crianca)

def vacina_create(request):
    vacina = VacinaForm(request.POST or None)
    if vacina.is_valid():
        vacina.save()
        return redirect('index')
    return render(request, 'vacina/form.html', {'form': vacina})

def vacina_update(request, id):
    vacina = VacinaDAO.find_one(id)
    form = VacinaForm(request.POST or None, instance=vacina)
    if form.is_valid():
        form.save()
        return redirect('index')
    return render(request, 'vacina/form.html', {'vacina': vacina})

def vacina_index(request):
    lista_vacinas = VacinaDAO.find_all()
    return render(request, 'vacina/index.html', {'lista_vacinas': lista_vacinas})

def vacina(request, id):
    result =  VacinaDAO.find_one(id)
    return render(
        request,
        'vacina/detail.html',
        {'vacina': result}
        )

def delete_vacina(request, id):
    result = VacinaDAO.delete(id)
    return redirect('index')
