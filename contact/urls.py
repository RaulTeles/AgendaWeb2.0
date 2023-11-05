from django.urls import path, include
from contact import views
#importando a função static para criar a url media
from django.conf.urls.static import static
#importando configurações do arquivos settings.py
from django.conf import settings

app_name = 'contact'

urlpatterns = [
    path('', views.index, name='index'),
    path('search/', views.search, name='search'),

    #orientações e recomendações para a fomatar a url (CRUD)

    path('contato/<int:contact_id>/detail', views.contatos, name='contatos'), #Read

    path('contato/create/', views.create, name='create'), #Create

    path('contato/<int:contact_id>/update', views.update, name='update'), #update
    
    path('contato/<int:contact_id>/delete', views.delete, name='delete'), #delete

    #url de resgistro
    path('user/create/', views.register, name='register'), #Create

]

#informando o caminho da pasta media onde contém os arquivos
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
#informando o caminho da pasta static onde contém os arquivos
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
