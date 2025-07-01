import random
import string

def senha(value):

    if value <= 0:
        return "Digite um número positivo"


    caracteres = string.printable

    senha = ''.join(random.choice(caracteres) for _ in range(value))

    return senha

caracteres = int(input("Digite o tamnaho da senha que deseja em números: "))
nova_senha = senha(caracteres)

print(nova_senha)