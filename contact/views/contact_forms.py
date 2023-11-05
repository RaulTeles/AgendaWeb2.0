# Criando o metodo contact_forms para criação de views com função de criar coisas, seguindo o modelo do CRUD
#importando o biblioteca get_objetct_or_400 para criar uma exceção para o erro de página não encontrada
#importando o redirect para ser utilizado na view seach, caso um usuario procure algo que não existe será redirecionado para o index
from django.shortcuts import get_object_or_404, render, redirect
#importando a classe contact criada la no arquivo models
from contact.models import contact
#importando a classe do fomulário no arquivo form
from contact.forms import contactForms
#importando a função reverse, para deixar a url do post dinamica
from django.urls import reverse


def create(request):

    form_action = reverse('contact:create')

    if request.method == 'POST':

        formulario = contactForms(request.POST, request.FILES)

        context = {
        #passando o formulário no contexto para poder ser mostrado no html
        'form' : formulario,
        'form_action' : form_action
        }

        #veiricando se o formato é válido para salvar o formulário criado

        if formulario.is_valid():
            contato = formulario.save()

            #fazendo uma requisição para quando o relatorio for enviado, a página seja atualizada para os nomes não ficarem nos campos
            return redirect('contact:update',contact_id=contato.pk)



        return render(request,
            'contact/create.html',
            context,
            )



    context = {
        #passando o formulário no contexto para poder ser mostrado no html
        'form' : contactForms(),
        'form_action' : form_action

    }

    return render(request,
                'contact/create.html',
                context,
                )



def update(request, contact_id):
    
    contato = get_object_or_404(contact,pk=contact_id,show=True)

    form_action = reverse('contact:update', args=(contact_id,))

    if request.method == 'POST':

        formulario = contactForms(request.POST, request.FILES, instance=contato)

        context = {
        #passando o formulário no contexto para poder ser mostrado no html
        'form' : formulario,
        'form_action' : form_action
        }

        #veiricando se o formato é válido para salvar o formulário criado

        if formulario.is_valid():
            contato = formulario.save()

            #fazendo uma requisição para quando o relatorio for enviado, a página seja atualizada para os nomes não ficarem nos campos
            return redirect('contact:update',contact_id=contato.pk)



        return render(request,
            'contact/create.html',
            context,
            )

    context = {
        #passando o formulário no contexto para poder ser mostrado no html
        'form' : contactForms(instance=contato),
        'form_action' : form_action,
    }

    return render(request,
                'contact/create.html',
                context,
                )

def delete(request,contact_id):
    contato = get_object_or_404(contact,pk=contact_id,show=True)

    confirmation = request.POST.get('confirmation', 'no')
    if confirmation == 'yes':
        contato.delete()
        return redirect('contact:index')

    return render(request,
                'contact/contact.html',
                {
                    'pagina_contato' : contato,
                    'confirmation' : confirmation,
                }
                )