import requests


def consultar_cep(value):
    URL = f"https://viacep.com.br/ws/{value}/json/"

    # print(value)

    response = requests.get(URL)

    dados = response.json()
    end = f"""
    logradouro: {dados["logradouro"]}
    bairro: {dados["bairro"]}
    cidade: {dados["localidade"]}
    estado: {dados["estado"]}
    """

    return end


cep = input("Digite seu cep: ").replace("-","")

result = consultar_cep(cep)

print(result)

