from django.shortcuts import render

from django.http import HttpResponse

from pagControle.models import Cliente

def index(request):
    clientes = Cliente.objects.all()
    context = {'clientes':clientes}
    return render(request, 'index.html', context)


