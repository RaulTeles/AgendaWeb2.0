from django.db import models
#importando a biblioteca timezone para utilizar no campo da data
from django.utils import timezone
#importando classe User para fazer autenticação do usuário para os contatos, está sendo utilizando no owner
from django.contrib.auth.models import User


#Sempre quando alterar algo nos models, utilizar o comando python manage.py makemigrations

#é necessário registrar o model no admin

# Create your models here.

#Criando o model Categoria
class Category(models.Model):
    #utiizando classe Meta (já é padrão do django) para alterar os nomes padrões criados na parte admin da pag
    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
    name = models.CharField(max_length=20)
    
    def __str__(self) -> str:
        return (f'{self.name}')
    

#Criando classe contactpara o model
class contact(models.Model):
    #criando um campo para a tabela
    #Charfield equivale a uma string e logo após é passado a quantidade de caracteres que pode ser usádo no campo.
    #OBSERVAÇÃO: Por padrão todos os campos que recebem texto são campos obrigatórios.
    first_name = models.CharField(max_length=20)
    
    #criando uma strig para o ultimo nome (string)
    last_name = models.CharField(max_length=20)
    
    #criando uma string para telefone tipo string
    phone = models.CharField(max_length=15)
    
    #criando um campo de email especifico para o email | o parametro blank= True é para deixar o campo como opcional.
    email = models.EmailField(max_length=254, blank=True)
    
    #criando um campo para a data, o campo é definido automaticamente para o usuário não precisar digitar. utilizando o timezone para pegar a data e hora atual do pc 
    created_date = models.DateTimeField(default=timezone.now)
    
    #criando o campo de descrição como um campo texto
    description = models.TextField(blank=True)
    
    #Criando um campo para exbição ou não do contat, deixando pro padrão para exibição
    show = models.BooleanField(default=True)

    #Criando um campo para envio de imagens, o parâmentro upload_to é para setar qual a pasta onde sera enviado a imagem
    picture = models.ImageField(blank=True, upload_to='pictures/%Y/%m/')

    #criando um campo para se comunicar com o model categoria como uma chave estrangeira
    #on_delete, define o que será feito com os contatos quando apagar uma categoria
    category = models.ForeignKey(Category, on_delete=models.SET_NULL,blank=True, null=True)
    #criando campo para identificar qual usuário está criando o post
    owner = models.ForeignKey(User, on_delete=models.SET_NULL,blank=True, null=True)


    #criando um método __str__ para sobrescrever nomes automaticos lá pagina admin

    def __str__(self) -> str:
        return (f'{self.first_name} {self.last_name}')