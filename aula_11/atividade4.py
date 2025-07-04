import json

def escrita_json(value1, value2):

    with open(value1, "w", encoding="utf-8") as arquivo_escrito:
        json.dump(value2, arquivo_escrito, ensure_ascii=False, indent=4 )

        print("dados salvos")

    return arquivo_escrito



def leitor_json(value1, value2):
    arquivo = escrita_json(value1, value2)


    with open(value1, "r", encoding="utf-8") as arquivo:
        arquivo_lido = json.load(arquivo)

        print(arquivo_lido)
 
    return



dados = {
    "nome": "Danilo",
    "idade": "32",
    "cidade": "Natal"
}


arquivo = input("Digite o nome que será salvo: ").strip().replace("-", "_") 

arquivo_json = leitor_json(arquivo, dados)
