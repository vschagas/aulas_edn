import csv

def leitor_csv(value):
    
    with open(value, "r", newline="", encoding="utf-8") as arquivo:
        leitor = csv.reader(arquivo)

        result = []

        for dado in leitor:
            result.append(dado)

    return result



arquivo = input("Digite o nome do arquivo: ").strip()

print(leitor_csv(arquivo))