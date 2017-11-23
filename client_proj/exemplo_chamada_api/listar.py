import requests

try:
    response = requests.get("http://localhost:8000/cliente/")

    if response.status_code == 200:
        print("OK")
    else:
        print("Erro: %s" % response.status_code)
    print("Resposta: %s\n" % response.content)

    print("Registros")
    json = response.json()
    for linha in json:
        for col in linha:
            print('%s: %s' % (col, linha[col]))
        print()

except requests.exceptions.ConnectionError:
    print("Serviço indisponível (ConnectionError)")

