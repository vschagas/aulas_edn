import datetime

def idade_em_dias(ano_nascimento):


    ano_atual = datetime.datetime.now().year

    idade = ano_atual - ano_nascimento
    dias = idade * 365
    
    return dias

result = idade_em_dias(2023)

print(result)