from django.core.paginator import Paginator
from django.shortcuts import redirect, render
from core.dao import (
    CriancaDAO,
    VacinaDAO,
    VacinacaoDAO
)
from .forms import (
    CriancaForm,
    VacinaForm,
    VacinacaoForm,
)
from .utils import Utils

# Crianca views
def crianca_index(request):
    lista_criancas = CriancaDAO.find_all()  # Solicitando todos registro de Crianca
    paginator = Paginator(
        lista_criancas,
        10
    )  # Paginando a lista de criancas
    # Pegando a pagina atual por parametro da aquisicao HTTP
    page_number = request.GET.get('page')
    # Pegando somento os dados da pagina atual
    page_obj = paginator.get_page(page_number)
    # Separando lista de criancas dos outros dados da paginacao
    lista_criancas = page_obj.object_list

    return render(
        request,
        'crianca/index.html',
        {
            'lista_criancas': lista_criancas,
            'paginator': page_obj
        }
    )


def crianca_create(request):
    # Criando uma instancia do Form Crianca com dados vindos por requisicao HTTP
    try:
        print(request.POST['cpf'])
        _mutable = request.POST._mutable
        request.POST._mutable = not _mutable
        cpf_with_mask = request.POST['cpf']
        cpf_without_mask = Utils.remove_cpf_mask(cpf_with_mask)
        request.POST['cpf'] = cpf_without_mask
        request.POST._mutable = _mutable
    except Exception:
        pass
    crianca = CriancaForm(request.POST or None)

    if request.method == 'POST':  # Verificando se esta sendo solicitado cadastramento de uma nova crianca
        if crianca.is_valid():  # Verificando se a instancia possui campos validos de acordo com o Model
            crianca.save()  # Salvando objeto
            # #Redirecionando o cliente para pagina inicial
            return redirect('index')

    return render(
        request,
        'crianca/form.html',
        {'form': crianca}
    )


def crianca_update(request, id):
    # Pegando o objeto que foi solicitado editar
    try:
        print(request.POST['cpf'])
        _mutable = request.POST._mutable
        request.POST._mutable = not _mutable
        cpf_with_mask = request.POST['cpf']
        cpf_without_mask = Utils.remove_cpf_mask(cpf_with_mask)
        request.POST['cpf'] = cpf_without_mask
        request.POST._mutable = _mutable
    except Exception:
        pass
    crianca = CriancaDAO.find_one(id)
    form = CriancaForm(
        request.POST or None,
        instance=crianca
    )  # Criando um form com dados vindos por requisicao HTTP
    print(crianca.cpf)
    if request.method == 'POST':  # Verificando se esta sendo solicitado mudanca dos dados
        if form.is_valid():  # Verificando se a instancia possui campos validos de acordo com o Model
            form.save()  # Salvando objeto
            # Redirecionando o cliente para pagina inicial
            return redirect('index')

    return render(
        request,
        'crianca/form.html',
        {'crianca': crianca}
    )


def crianca_delete(request, id):
    crianca = CriancaDAO.find_one(id)
    if request.method == "POST":  # Confirmando se o method da requisicao e POST para confirmar a exclusao
        CriancaDAO.delete(crianca.id)  # Solicitando a exclusao no BD
        # Redirecionando o cliente para pagina inicial
        return redirect('index')


# Vacinacao views
def vacinacao_index(request, id):
    # Pegando objeto que foi solicitado a lista de vacinacao
    crianca = CriancaDAO.find_one(id)
    # Criando um formulario de vacinacao
    form = VacinacaoForm(request.POST or None)
    # Pegando todos registros de vacinas, para auxlior no formulario
    vacinas = VacinaDAO.find_all()

    if request.method == 'POST':  # Verificando se esta sendo solicitado cadastramento de uma nova vacinacao
        if form.is_valid():  # Verifica se os dados estao de acordo com os solicitados pelo Model,
            form.save()  # Salvando nova vacinacao
            return redirect(
                'vacinacao_index',
                id=id
            )  # recarregando a pagina de vacinacao

    # Pegando todas vacinacoes da Crianca solicitada
    lista_vacinacao = CriancaDAO.get_vacincas(id)

    paginator = Paginator(
        lista_vacinacao,
        10
    )  # Paginando a lista de crianca
    # Pegando a pagina atual por parametro da aquisicao HTTP
    page_number = request.GET.get('page')
    # Pegando somento os dados da pagina atual
    page_obj = paginator.get_page(page_number)
    # Separando lista de vacinacoes dos outros dados da paginacao
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
    # Pegando a vacinacao que foi solicitada exclusao
    vacinacao = VacinacaoDAO.find_one(id)
    if request.method == 'POST':  # Verificando se o usuario estar confirmando a exclusao
        # Guardando o ID da crianca a quem pertence a vacinacao
        id_crianca = vacinacao.crianca.id
        VacinacaoDAO.delete(vacinacao.id)  # Excluindo a vacinacao
        # Recarregando pagina de lista de vacinacoes
        return redirect('vacinacao_index', id=id_crianca)


#Vacina views
def vacina_index(request):
    lista_vacinas = VacinaDAO.find_all()
    return render(
        request,
        'vacina/index.html',
        {'lista_vacinas': lista_vacinas}
    )


def vacina_create(request):
    # Criando um formulario de Vacina com dados vindos por requisicao HTTP
    vacina = VacinaForm(request.POST or None)

    if vacina.is_valid():  # Verificando se a instancia possui campos validos de acordo com o Model
        vacina.save()  # Salvando nova vacina
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
    vacina = VacinaDAO.find_one(id)
    if request.method == "POST":  # Confirmando se o method da requisicao e POST para confirmar a exclusao
        VacinaDAO.delete(vacina.id)  # Solicitando a exclusao no BD
        # Redirecionando o cliente para lista da vacinas
        return redirect('vacina_index')
