# Criando o metodo contact_forms para criação de views com função de criar coisas, seguindo o modelo do CRUD
#importando o biblioteca get_objetct_or_400 para criar uma exceção para o erro de página não encontrada
#importando o redirect para ser utilizado na view seach, caso um usuario procure algo que não existe será redirecionado para o index
#importando a classe contact criada la no arquivo models
from contact.models import contact

#importando a biblioca form para utilização das classes
from django import forms
#importando o model padrão do djagno USER  para usar os campos 
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
from django.contrib.auth import password_validation


##################################################################################################

#Criando uma classe para os formulários
#passando o parametro ModelForm, pq o formulário vai ser criado em base aos models já existentes

class contactForms(forms.ModelForm):

    #criando uma outra forma de widget, necessário criar um campo já existente
    #widget basicamente é para alterar o html, porem utilizando o django

    picture = forms.ImageField(
        widget=forms.FileInput(
            attrs={
                'accept' : 'image/*',
            }
        )
    )

    first_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'placeholder' : 'Digite o seu primeiro nome!'
            }
        ),  label='Pimeiro nome:',
            help_text='Texto de ajuda!',
    )

    last_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'placeholder' : 'Digite o seu Sobrenome!',
            }
        ), label='Sobrenome:'
    )

    #criando um init e passando o args e o kwargs, pois não pretendo passar a quantidade de argumentos,
    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)

    # #Criando outra forma para usar os widget        
    #     self.fields['first_name'].widget.attrs.update(
    #         {
    #             'placeholder':'Digite o seu primeiro nome!'
    #         }
    #     )


    class Meta:
        #definindo qual é model em que o formulário será criado
        model = contact
        #definindo quais campos serão exibidos nos forms
        fields = ('first_name','last_name','phone','email','description','category','picture')

        #criando um widget no formulário (personalizando os campos)

        # widgets = {
        #     'first_name' : forms.TextInput(

        #         # o attrs é referente aos atributos do widgets e recebe chave e valor igual o widgets
        #         attrs={
        #             'placeholder' : 'Digite o seu primeiro nome!!',
        #         }
        #     ) 
        # }

    #O método clean ele é criado para ser chamado antes de criar qualquer coisa na base de dados
    
    def clean(self):

        # #criando método para criar a mensagem e erro
        # self.add_error(
        #     'first_name',
        #     ValidationError(
        #         'Mensagem de error',
        #         code='invalid'
        #     )
        # )
        return super().clean()
    
    #Validando um campo no formulário

    def clean_first_name(self):
        first_name = self.cleaned_data.get('first_name')
        


        if first_name == 'ABC':

            self.add_error(
            'first_name',
            ValidationError(
                'Não pode ser digitado ABC!',
                code='invalid'
            )
        )
            
            # #Exemplo de validaçãode um campo expecifico
            # raise ValidationError('Não pode digitar ABC')
            
        return first_name
        
class RegisterForm(UserCreationForm):

    #criando widget para adicinar os campos obrigatorios

    first_name = forms.CharField(
        required=True,
        min_length=3,
    )
    last_name = forms.CharField(
        required=True,
        min_length=3,
    )
    email = forms.EmailField(
        required=True
    )

    
    class Meta:
        model = User
        #informando os fiels (são tuplas)
        fields = ('first_name',
                'last_name',
                'email',
                'username',
                'password1',
                'password2')
        
    #criando um método clean_email para garantir que não vai ter usuários com emails repetidos

    def clean_email(self):

        email = self.cleaned_data.get('email')

        #checando se já tem usuário na base de dados
        if User.objects.filter(email=email).exists():
            self.add_error(
                'email',
                ValidationError('Já existe esse E-mail', code='invalid')
            )

        return email

class RegisterUpdateForm(forms.ModelForm):

    first_name = forms.CharField(
        min_length=2,
        max_length=30,
        required=True,
        help_text='Required.',
        error_messages={
            'min_length': 'Please, add more than 2 letters.'
        }
    )
    last_name = forms.CharField(
        min_length=2,
        max_length=30,
        required=True,
        help_text='Required.'
    )

    password1 = forms.CharField(
        label="Password",
        strip=False,
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password"}),
        help_text=password_validation.password_validators_help_text_html(),
        required=False,
    )

    password2 = forms.CharField(
        label="Password 2",
        strip=False,
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password"}),
        help_text='Use the same password as before.',
        required=False,
    )
    class Meta:
        model = User
        fields = ('first_name',
                'last_name',
                'email',
                'username',
                )