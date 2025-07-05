from pymongo import MongoClient

URI = "mongodb+srv://valmir:X2QvyR3NfaRAeqB9@cluster0.kj6hvkk.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

client = MongoClient(URI)
db = client["clientes"]
colecao = db["users"]

def update_user(value):

    response = colecao.update_one(
        {"nome": value["nome"]},
        {"$set": value}
    )

    return "Usuário atualizado com Sucesso"

user = {
    "nome": "Walter",
    "idade": 16,
    "altura": 168,
    "time_favoritos": ["remo", "paissandu", "botafogo"],
    "cpf": "000.000.000-00"
}

result = update_user(user)

print(result)


