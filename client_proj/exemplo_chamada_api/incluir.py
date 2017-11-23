import requests

dados = {"nome": "João", "email": "john11@doe.com"}
try:
    response = requests.post("http://localhost:8000/cliente/", data=dados)

    if response.status_code == 201:
        print("Cliente incluído com sucesso")
    else:
        print("Erro: %s" % response.status_code)
    print("Resposta: %s\n" % str(response.content))

    print("Registro")
    registro = response.json()
    for nome_campo in registro:
        print('%s: %s' % (nome_campo, registro[nome_campo]))

except requests.exceptions.ConnectionError:
    print("Serviço indisponível (ConnectionError)")

