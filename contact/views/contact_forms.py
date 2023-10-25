# Criando o metodo contact_forms para criação de views com função de criar coisas, seguindo o modelo do CRUD

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


def create(request):


    context = {

    }

    return render(request,
                'contact/create.html',
                context,
                )