import requests

try:
    response = requests.get("http://localhost:8000/cliente/1/")

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

