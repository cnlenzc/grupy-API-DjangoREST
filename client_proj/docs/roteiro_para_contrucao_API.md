# Roteiro para construção da API REST

#### Criar e ativar o ambiente virtual do python
```
$ mkdir pythonista_api
$ cd pythonista_api
$ virtualenv —python=python3 env
$ source env/bin/activate
```

#### Instalar as dependências (pacotes do python)
```
pip install django
pip install djangorestframework
```


#### Criar o projeto e app do Django
```
django-admin.py startproject pythonista_proj
cd pythonista_proj
python manage.py startapp pythonista
```


#### Testar o servidor Http
```
python manage.py runserver
```
Abra o browser com url
http://localhost:8000/


#### Adicione o app na lista de apps instalados
Adicione também o app da rest_framework
Arquivo pythonista_proj/setting.py
```
INSTALLED_APPS = [
   …
    'rest_framework',
    'pythonista',
]
```


#### Crie sua primeira view em Django
Arquivo pythonista_proj/view.py
```
from django.http import HttpResponse

def index(request):
    return HttpResponse("Olá Pytonistas! Bem vindo ao Grupy!")


Adicione a view na lista de url do app
Arquivo pythonista/urls.py
———————————————————
from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
]
```


#### Adicione a lista de url do app na lista de url do projeto
Arquivo pythonista_proj/urls.py
```
from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'^', include('pythonista.urls')),
    url(r'^admin/', admin.site.urls),
]
```


#### Teste novamente o servidor e veja se se a view apresenta a frase corretamente
```
control+C
python manage.py runserver
http://localhost:8000/
```


#### Construção do Modelo de Objetos (models.py)
Obs: O modelo relacional (BD) é gerado pelo Django a partir do modelo de objetos.
Arquivo pythonista/models.py
```
from django.db import models

enum_sexo = (('M', 'Masculino'), ('F', 'Feminino'), ('O', 'Outro'))

class Pythonista(models.Model):
    nome = models.CharField(max_length=50, null=False)
    email = models.EmailField(null=False)
    telefone = models.CharField(max_length=15, null=True)
    sexo = models.CharField(choices=enum_sexo, max_length=1, null=True)
    site = models.URLField(null=True)
```


#### Criação do Banco Relacional
```
python manage.py makemigrations
python manage.py migrate
```

#### Consultar os comandos SQL gerados pelo Django
```
python manage.py sqlmigrate pythonista 0001
```

#### Criando o primeiro pythonista
```
python manage.py shell
from pythonista.models import Pythonista
c = Pythonista(nome='Pedro', email='pedro@g.com')
c.save()
```

#### Shell SQL do sqlite
```
python manage.py dbshell
.table
.schema pythonista_pythonista
select * from pythonista_pythonista;
.header on
.mode column
.exit
```

#### Configuração da Rota URL
Arquivo pythonista/urls.py
```
from django.conf.urls import url
from pythonista import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^pythonista/$', views.PythonistaList.as_view()),
]
```


#### Criação da view
Arquivo pythonista/views.py
```
from django.http import HttpResponse
from rest_framework import generics
from pythonista.models import Pythonista
from pythonista.serializers import PythonistaSerializer

def index(request):
    return HttpResponse("Olá Pytonistas! Bem vindo ao Grupy!")

class PythonistaList(generics.ListCreateAPIView):
    '''
    Este método realiza 2 operações de acordo com o método Http:
    GET - consulta lista de pythonistas
    POST - inclui um novo pythonista
    '''
    queryset = Pythonista.objects.all()
    serializer_class = PythonistaSerializer

class PythonistaDetail(generics.RetrieveUpdateDestroyAPIView):
    '''
    Este método realiza 3 operações de acordo com o método Http:
    GET - consulta pythonista
    PUT - altera dados do pythonista
    DELETE - remove pythonista
    '''
    queryset = Pythonista.objects.all()
    serializer_class = PythonistaSerializer
```


#### Criação do serializer
Arquivo pythonista/serializers.py
```
from rest_framework import serializers
from pythonista.models import Pythonista

class PythonistaSerializer(serializers.ModelSerializer):
   class Meta:
        model = Pythonista
        fields = ('__all__')
```

#### Chamando a API pela linha de comando
```
curl localhost:8000/pythonista/
curl -i localhost:8000/pythonista/
http get localhost:8000/pythonista/
```

#### Chamando a API em outro programa python
```
import requests
# listar
response = requests.get("http://localhost:8000/pythonista/")
print(response.content)

# incluir
dados = {"nome": "João", "email": "john11@doe.com"}
response = requests.post("http://localhost:8000/pythonista/", data=dados)
print(response.content)

# consultar
response = requests.get("http://localhost:8000/pythonista/1/")
print(response.content)

# extraindo os valores
registro = response.json()
registro['nome']
registro[‘email’]
for nome_campo in registro:
    print('%s: %s' % (nome_campo, registro[nome_campo]))
```
