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

#Crianca views
def crianca_index(request):
    lista_criancas = CriancaDAO.find_all() #Solicitando todos registro de Crianca
    paginator = Paginator(
        lista_criancas,
        10
    ) #Paginando a lista de criancas
    page_number = request.GET.get('page') #Pegando a pagina atual por parametro da aquisicao HTTP
    page_obj = paginator.get_page(page_number) #Pegando somento os dados da pagina atual
    lista_criancas = page_obj.object_list #Separando lista de criancas dos outros dados da paginacao

    return render(
        request,
        'crianca/index.html',
        {
            'lista_criancas': lista_criancas,
            'paginator': page_obj
        }
    )

def crianca_create(request):
    crianca = CriancaForm(request.POST or None) #Criando uma instancia do Form Crianca com dados vindos por requisicao HTTP

    if request.method == 'POST': #Verificando se esta sendo solicitado cadastramento de uma nova crianca
        if crianca.is_valid(): #Verificando se a instancia possui campos validos de acordo com o Model
            crianca.save() #Salvando objeto
            return redirect('index') #Redirecionando o cliente para pagina inicial

    return render(
        request,
        'crianca/form.html',
        {'form': crianca}
    )

def crianca_update(request, id):
    crianca = CriancaDAO.find_one(id) #Pegando o objeto que foi solicitado editar
    form = CriancaForm(
        request.POST or None,
        instance=crianca
    ) #Criando um form com dados vindos por requisicao HTTP

    if request.method == 'POST': #Verificando se esta sendo solicitado mudanca dos dados
        if form.is_valid(): #Verificando se a instancia possui campos validos de acordo com o Model
            form.save() #Salvando objeto
            return redirect('index') #Redirecionando o cliente para pagina inicial

    return render(
        request,
        'crianca/form.html',
        {'crianca': crianca}
    )

def crianca_delete(request, id):
    if request.method == "POST": #Confirmando se o method da requisicao e POST para confirmar a exclusao
        CriancaDAO.delete(id) #Solicitando a exclusao no BD
        return redirect('index') #Redirecionando o cliente para pagina inicial

#Vacinacao views
def vacinacao_index(request, id):
    crianca = CriancaDAO.find_one(id) #Pegando objeto que foi solicitado a lista de vacinacao
    form = VacinacaoForm(request.POST or None) #Criando um formulario de vacinacao
    vacinas = VacinaDAO.find_all() #Pegando todos registros de vacinas, para auxlior no formulario

    if request.method == 'POST': #Verificando se esta sendo solicitado cadastramento de uma nova vacinacao
        if form.is_valid(): #Verifica se os dados estao de acordo com os solicitados pelo Model,
            form.save() #Salvando nova vacinacao
            return redirect(
                'vacinacao_index',
                id=id
            ) #recarregando a pagina de vacinacao
    
    lista_vacinacao = CriancaDAO.get_vacincas(id) #Pegando todas vacinacoes da Crianca solicitada

    paginator = Paginator(
        lista_vacinacao,
        10
    )#Paginando a lista de crianca
    page_number = request.GET.get('page') #Pegando a pagina atual por parametro da aquisicao HTTP
    page_obj = paginator.get_page(page_number) #Pegando somento os dados da pagina atual
    lista_vacinacao = page_obj.object_list #Separando lista de vacinacoes dos outros dados da paginacao
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
    vacinacao = VacinacaoDAO.find_one(id) #Pegando a vacinacao que foi solicitada exclusao
    if request.method == 'POST': #Verificando se o usuario estar confirmando a exclusao
        id_crianca = vacinacao.crianca.id #Guardando o ID da crianca a quem pertence a vacinacao
        VacinacaoDAO.delete(vacinacao.id) #Excluindo a vacinacao
        return redirect('vacinacao_index', id=id_crianca) #Recarregando pagina de lista de vacinacoes

def vacina_index(request):
    lista_vacinas = VacinaDAO.find_all()
    return render(
        request,
        'vacina/index.html',
        {'lista_vacinas': lista_vacinas}
    )
    
def vacina_create(request):
    vacina = VacinaForm(request.POST or None) #Criando um formulario de Vacina com dados vindos por requisicao HTTP

    if vacina.is_valid(): #Verificando se a instancia possui campos validos de acordo com o Model
        vacina.save() #Salvando nova vacina
        return redirect('vacina_index')

    return render(
        request,
        'vacina/form.html',
        {'form': vacina}
    )

def vacina_update(request, id):
    vacina = VacinaDAO.find_one(id)
    form = VacinaForm(
        request.POST or None,
        instance=vacina
    )
    if form.is_valid():
        form.save()
        return redirect('vacina_index')
    return render(
        request,
        'vacina/form.html',
        {'vacina': vacina}
    )


def vacina_delete(request, id):
    result = VacinaDAO.delete(id)
    return redirect('vacina_index')
