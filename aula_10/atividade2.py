from faker import Faker
# fake = Faker(['it_IT', 'en_US', 'ja_JP'])


fake = Faker("pt_BR")

def gerar_usuario():
    # for _ in range(5):
    #     print(fake.name())

    nome = fake.name()
    email = fake.email()
    cpf = fake.cpf()
    pais = fake.current_country()

    user = f"""
    nome: {nome}
    email: {email}
    cpf: {cpf}
    país: {pais}
    """

    return user


usuario = gerar_usuario()

print(usuario)