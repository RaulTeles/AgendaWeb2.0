#importando o biblioteca get_objetct_or_400 para criar uma exceção para o erro de página não encontrada
from django.shortcuts import get_object_or_404, render
#importando a classe contact criada la no arquivo models
from contact.models import contact
#importando a biblioteca para adicionar uma exceção para o erro 404, mesma coisa do get_object_or_404
from django.http import Http404


def index(request):
    #Utilizando os models para buscar as informações dos contatos e apresentar na página
    #criando uma variavel contacts para buscar os valores do models
    #filtrando os contatos que o campo show está como Verdadeiro
    contacts = contact.objects.filter(show=True).order_by('-id')

    #criando uma váriavel para usar no render como contexto
    context = {
        'contacts_chave' : contacts,
    }

    return render(request,
                'contact/index.html',
                context,
                )

def contatos(request, contact_id):

    #.get retorna um unico valor
    # single_contact = contact.objects.filter(pk=contact_id).first()
#adicionando uma exceção para erro caso pesquise alguma url que não existe
    # if single_contact is None:
    #     raise Http404()

# Criando uma outra forma para criar a exceção do erro 404
    single_contact = get_object_or_404(contact.objects, pk=contact_id, show=True)

    context = {
        'pagina_contato' : single_contact,
    }
    return render(request,
                'contact/contact.html',
                context,
                )
