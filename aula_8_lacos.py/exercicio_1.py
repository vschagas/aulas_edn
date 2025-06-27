
def calculadora():

    try:
        numero_1 = float(input("Digite o primeiro número "))
        numero_2 = float(input("Digite o segundo número "))
        operacao = input("Digite uma das opcoes (+, -, /, *) ")

        if operacao == "+":
            print(numero_1 + numero_2)

        elif operacao == "-":
            print(numero_1 - numero_2)

        elif operacao == "/":
            print(numero_1 / numero_2)

        elif operacao == "*":
            print(numero_1 * numero_2)
        else:
            print("Operação inválida")

    except ValueError:
        print("Digite apenas números")
    except ZeroDivisionError:
        print("Error! Não é possível dividir por zero")

calculadora()

