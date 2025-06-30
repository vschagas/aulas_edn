def calcular_gorjeta(porcentagem_gorjeta, conta):
    # porcentagem_gorjeta = float(input("Digite o valor da gorjeta em %: "))
    # conta = float(input("Digite o valor da conta: "))

    gorjeta = (porcentagem_gorjeta / 100)
    total = (gorjeta * conta) + conta

    # print(total)
    return total


result = calcular_gorjeta(10, 100)

print(result)