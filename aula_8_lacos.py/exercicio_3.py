notas = []

while True:
    try:
        senha = input("Digite uma senha ou sair para terminar: ").lower()

        if senha == "sair":
            break
        if len(senha) < 8:
            print("sua senha deve ter pelo menos 8 caracteres")
        # notas.append(float(nota))
            continue 
        if not any(caractere.isdigit() for caractere in senha):
            print("essa senha é fraca")
            continue

        print(senha)
        break
    except ValueError:
        print("operação inválida")
  

