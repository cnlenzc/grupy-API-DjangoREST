import requests

dados = {"nome": "João", "email": "john9@doe.com"}
try:
    response = requests.put("http://localhost:8000/cliente/1/", data=dados)

    if response.status_code == 200:
        print("OK")
    else:
        print("Erro: %s" % response.status_code)
    print("Resposta: %s\n" % response.content)

    print("Registro")
    json = response.json()
    for col in json:
        print('%s: %s' % (col, json[col]))

except requests.exceptions.ConnectionError:
    print("Serviço indisponível (ConnectionError)")

