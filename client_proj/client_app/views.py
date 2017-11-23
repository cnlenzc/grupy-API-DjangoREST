from django.http import HttpResponse
from rest_framework import generics
from client_app.models import Cliente
from client_app.serializers import ClienteSerializer


def index(request):
    return HttpResponse("Olá Pytonistas! Bem vindo ao Grupy!")


class ClienteList(generics.ListCreateAPIView):
    '''
    Este método realiza 2 operações de acordo com o método Http:
    GET - consulta lista de clientes
    POST - inclui um novo cliente
    '''
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer


class ClienteDetail(generics.RetrieveUpdateDestroyAPIView):
    '''
    Este método realiza 3 operações de acordo com o método Http:
    GET - consulta cliente
    PUT - altera dados do cliente
    DELETE - remove cliente
    '''
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer
