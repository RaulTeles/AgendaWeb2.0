from django.contrib import admin
#importando todos os models do arquivo model do app contact
from  contact import models

# Register your models here.

#criando class para registrar o model
#utilizando o decorator e passando a classe criada no models como parametro
@admin.register(models.contact)
class contactAdmin(admin.ModelAdmin):
    #definindo quais o campos eu estou querendo mostrar na parte admin dos contatos
    list_display = ('id','first_name', 'last_name', 'phone','show',)
    #definindo uma lista para editar
    list_editable = ('show',)
    #definindo a ordem padrão do campo especifico
    ordering = ('-id',)
    #adicionando um filtro na parte adm
    # list_filter = ('created_date',)
    #adicionando campo de pesquisa
    search_fields = ('id', 'first_name', 'last_name')
    #definindo a quantidade de itens será mostrado pro pagina
    list_per_page = 10
    #definindo o valor maximo dos itens mostrado 
    list_max_show_all = 200

#Registrando o model Categiria para aparecer no campo adm
@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    ordering = ('id',)