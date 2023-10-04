from datetime import date
import json
from django.shortcuts import redirect, render

from django.http import HttpResponse, JsonResponse

from pagControle.models import Cliente

def index(request):
    clientes = Cliente.objects.all()
    context = {'clientes':clientes}
    return render(request, 'index.html', context)

def cadastro_cliente(request):
    nome = request.POST['nome']
    login = request.POST['login']
    senha = request.POST['senha']
    novoCliente = Cliente(
        nome = nome,
        login = login,
        senha = senha,
        ativo = False,
        vencimento =  date.today(),
        plano = None
    )
    novoCliente.save()
    return redirect('http://127.0.0.1:8000/')

def deletar_cliente(request, pk):
    cliente = Cliente.objects.get(id=pk)
    cliente.delete()
    return redirect('http://127.0.0.1:8000/')

def editar_cliente(request, pk):
    cliente = Cliente.objects.get(id=pk)
    if request.method == 'POST':
        nome = request.POST['nome']
        login = request.POST['login']
        senha = request.POST['senha']
        cliente.nome = nome
        cliente.login = login
        cliente.senha = senha
        cliente.save() 
        return redirect('http://127.0.0.1:8000/')
    context = {'cliente':cliente}
    return render(request, 'editar_cliente.html', context)


def editar_cliente_modal(request, pk):
    cliente = Cliente.objects.get(id=pk)
    newdata = {
			"nome": cliente.nome,
            "login": cliente.login,
            "senha": cliente.senha
		}
    return JsonResponse(newdata)
