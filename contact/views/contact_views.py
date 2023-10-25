#importando o biblioteca get_objetct_or_400 para criar uma exceção para o erro de página não encontrada
#importando o redirect para ser utilizado na view seach, caso um usuario procure algo que não existe será redirecionado para o index
from django.shortcuts import get_object_or_404, render, redirect
#importando a classe contact criada la no arquivo models
from contact.models import contact
#importando a biblioteca para adicionar uma exceção para o erro 404, mesma coisa do get_object_or_404
from django.http import Http404
#importando a função Q para fazer o comparativo do OU na view de busca
from django.db.models import Q
#importando a função Paginator para criar uma paginação no site
from django.core.paginator import Paginator


##################################################################################################


def index(request):
    #Utilizando os models para buscar as informações dos contatos e apresentar na página
    #criando uma variavel contacts para buscar os valores do models
    #filtrando os contatos que o campo show está como Verdadeiro
    contacts = contact.objects.filter(show=True).order_by('-id')

    #criando o paginator nos index
    paginator = Paginator(contacts,10)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    #criando uma váriavel para usar no render como contexto
    context = {
        'page_obj' : page_obj,
        'site_nome' : 'Contatos - '
    }

    return render(request,
                'contact/index.html',
                context,
                )

##################################################################################################

def contatos(request, contact_id):

    #.get retorna um unico valor
    # single_contact = contact.objects.filter(pk=contact_id).first()
#adicionando uma exceção para erro caso pesquise alguma url que não existe
    # if single_contact is None:
    #     raise Http404()

# Criando uma outra forma para criar a exceção do erro 404
    single_contact = get_object_or_404(contact.objects, pk=contact_id, show=True)

    site_nome = f'{single_contact.first_name} {single_contact.last_name} - '

    context = {
        'pagina_contato' : single_contact,
        'site_nome' : site_nome
    }
    return render(request,
                'contact/contact.html',
                context,
                )
##################################################################################################

#Criando uma view para campo de pesquisa do site
def search(request):

    search_value = request.GET.get('q','').strip()

#utilizando o redirect para caso o usuario digite nenhum caracter, ele sere redirecionado para o index
    if search_value == '':
        return redirect('contact:index')
    
    #utilizando a função Q para procurar itens no campo search utilizando o OR 

    contacts = contact.objects.filter(show=True).filter(Q(first_name__icontains=search_value) |
                                                        Q(last_name__icontains=search_value)|
                                                        Q(phone__icontains=search_value)|
                                                        Q(email__icontains=search_value)
                                                        ).order_by('-id')
    
    
    paginator = Paginator(contacts,10)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    #criando uma váriavel para usar no render como contexto
    context = {
        'page_obj' : page_obj,
        'site_nome' : 'Search - '
    }

    return render(request,
                'contact/index.html',
                context,
                )