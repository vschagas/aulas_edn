notas = []

while True:
    try:
        nota = input("Digite a nota da turma ou fim para terminar: ").lower()

        if nota == "fim":
            break

        notas.append(float(nota))


        # print(notas)

    except ValueError:
        print("operação inválida")


resultado = sum(notas) / len(notas)
print(resultado)
