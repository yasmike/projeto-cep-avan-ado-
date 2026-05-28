import requests

resposta = requests.get("https://cep.awesomeapi.com.br/json/01001000")
print(resposta.json())

def buscar_cep(cep : str) -> dict:
    """
    a funçao recebe um cep , consulta um api e devolve informaçoes sobre o cep.
    """
    resposta = requests.get(f"https://cep.awesomeapi.com.br/json/{cep}" , timeout = 10)
    return resposta.json()

print(buscar_cep("06501115"))