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
#importando a biblioca form para utilização das classes
from django import forms
from django.core.exceptions import ValidationError


##################################################################################################

#Criando uma classe para os formulários
#passando o parametro ModelForm, pq o formulário vai ser criado em base aos models já existentes

class contactForms(forms.ModelForm):
    class Meta:
        #definindo qual é model em que o formulário será criado
        model = contact
        #definindo quais campos serão exibidos nos forms
        fields = ('first_name','last_name','phone')
    
    def clean(self):
        cleaned_data = self.cleaned_data

        self.add_error(
            'first_name',
            ValidationError(
                'Mensagem de error',
                code='invalid'
            )
        )



def create(request):

    if request.method == 'POST':
        context = {
        #passando o formulário no contexto para poder ser mostrado no html
        'form' : contactForms(request.POST),
        }


        return render(request,
            'contact/create.html',
            context,
            )



    context = {
        #passando o formulário no contexto para poder ser mostrado no html
        'form' : contactForms(),

    }

    return render(request,
                'contact/create.html',
                context,
                )