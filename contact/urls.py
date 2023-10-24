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
    path('<int:contact_id>/', views.contatos, name='contatos'),
]

#informando o caminho da pasta media onde contém os arquivos
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
#informando o caminho da pasta static onde contém os arquivos
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
