# def saudacao(nome, number):
#     print(nome, number)
    
#     return f"hello {nome} {number}"

# data = saudacao("valmir", 123)

# print(data)

######################################################

# def soma(a, b):
#     result = a + b
#     return result

# print(soma(10, 5))


######################################################

# sub = lambda a, b: a + b

# print(sub(2, 10))


######################################################


# calculo de IMC

# def calculo(number):

#     if result < 18.5:
#         return f" seu imc é {result:.2f} Abaixo do peso"
#     elif 18.5 <= result < 25:
#         return f"seu imc é {result:.2f} Peso normal"
#     elif 25 <= result < 30:
#         return f"seu imc é {result:.2f} Sobrepeso"
#     else:
#         return f"seu imc é {result:.2f} Obeso"


# def imc(peso, altura): 
#     result = float(peso / (altura ** 2))

#     calculo(result)

#     return result


# func = imc(70, 1.80)

# print( f"seu imc é {func}")







def calculo(number):

    if number < 18.5:
        return "Abaixo do peso"
    elif 18.5 <= number < 25:
        return "Peso normal"
    elif 25 <= number < 30:
        return "Sobrepeso"
    else:
        return "Obeso"


#######################################
def imc(value1, value2): 
    peso = value1
    altura = value2

    result = float(peso / (altura ** 2))

    classificacao = calculo(result)

    msg = f"seu imc é {result:.2f}, {classificacao} "

    return msg

func = imc(80, 1.80)

print(func)
