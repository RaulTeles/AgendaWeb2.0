# Criando o metodo contact_forms para criação de views com função de criar coisas, seguindo o modelo do CRUD
#importando o biblioteca get_objetct_or_400 para criar uma exceção para o erro de página não encontrada
#importando o redirect para ser utilizado na view seach, caso um usuario procure algo que não existe será redirecionado para o index
#importando a classe contact criada la no arquivo models
from contact.models import contact

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

        #criando método para criar a mensagem e erro
        self.add_error(
            'first_name',
            ValidationError(
                'Mensagem de error',
                code='invalid'
            )
        )
        return super().clean()