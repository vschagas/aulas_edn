import csv

def escrita_csv(value):

    with open(value, "w", newline= "", encoding="utf-8") as arquivo:
        escrita_csv = csv.writer(arquivo)
        escrita_csv.writerow(["nome", "idade", "cidade"])
        
        for dado in dados:
            escrita_csv.writerow(dado)



    return value

dados = [
    ["Ana", 28, "São Paulo"],
    ["João", 32, "Tocantins"],
    ["Pedro", 18, "Recife"],
    ["danilo", 25, "Recife"]
]


nome_arquivo = input("Digite o nome final do arquivo: ").strip().replace(" ", "_")

result = escrita_csv(nome_arquivo)
print(result)