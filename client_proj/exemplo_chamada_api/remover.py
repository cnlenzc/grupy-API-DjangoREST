import requests

try:
    response = requests.delete("http://localhost:8000/cliente/10/")

    if response.ok:
        print("OK")

    if response.status_code == 204:
        print("OK")
    else:
        print("Erro: %s" % response.status_code)
    print("Resposta: %s\n" % response.content)

except requests.exceptions.ConnectionError:
    print("Serviço indisponível (ConnectionError)")

