#importando a função redirect para utilizar quando houver a criação do usuário
from django.shortcuts import render, redirect
from contact.forms import RegisterForm
#importando uma função para enviar mensagens na página web
from django.contrib import messages


def register(request):

    formulario = RegisterForm(request.POST,)

    #vailidando o tipo de requisão para POST para confirmar a criação do usuário
    if request.method == 'POST':
        formulario = RegisterForm(request.POST,)

        if formulario.is_valid():
            formulario.save()
            messages.success(request,'Usuário criado com sucesso!')
            return redirect('contact:index')


    #o formulário de criação de conta está associado a função UserCreationForm importada no arquivo forms.py
    return render(request,
                'contact/register.html',
                {
                    'form' : formulario
                })