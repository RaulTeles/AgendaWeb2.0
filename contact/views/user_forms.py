#importando a função redirect para utilizar quando houver a criação do usuário
from django.shortcuts import render, redirect
from contact.forms import RegisterForm, RegisterUpdateForm
#importando uma função para enviar mensagens na página web, importando o auth para usar o método login para confirmar o login no formulario
from django.contrib import messages, auth
#importando função do django para criação de autenticação para fazer o login
from django.contrib.auth.forms import AuthenticationForm
#importando o decorator para deixar a view acessivel apaenas para quem estiver logado
from django.contrib.auth.decorators import login_required



def register(request):

    formulario = RegisterForm(request.POST,)

    #vailidando o tipo de requisão para POST para confirmar a criação do usuário
    if request.method == 'POST':
        formulario = RegisterForm(request.POST)

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

def login_view(request):

    login = AuthenticationForm(request)

    if request.method == 'POST':
        login = AuthenticationForm(request, data=request.POST)
            
        if login.is_valid():
            # messages.success(request, 'Login efetuado com sucesso!')
            user = login.get_user()
            auth.login(request, user)
            messages.success(request,'Login efetuado com sucesso!')
            return redirect('contact:index')
        else:
            messages.error(request,'Login inválido!')

    return render(request,
            'contact/login.html',
            {
                'form' : login,
            })

@login_required(login_url='contact:login_view')
def logout_view(request):

    auth.logout(request)

    messages.success(request, 'Você fez o logout!')
    return redirect('contact:login_view')

@login_required(login_url='contact:login_view')
def user_update(request):
    form = RegisterUpdateForm(instance=request.user)

    if request.method != 'POST':
        return render(
            request,
            'contact/user_update.html',
            {
                'form': form
            }
        )

    form = RegisterUpdateForm(data=request.POST, instance=request.user)

    if not form.is_valid():
        return render(
            request,
            'contact/user_update.html',
            {
                'form': form
            }
        )

    form.save()
    return redirect('contact:user_update')