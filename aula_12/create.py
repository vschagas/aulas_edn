from pymongo import MongoClient
from datetime import datetime

URI = "mongodb+srv://valmir:X2QvyR3NfaRAeqB9@cluster0.kj6hvkk.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

client = MongoClient(URI)
db = client["clientes"]
colecao = db["users"]


#INSERT EM MONGODB
    # banco.colecao.instrução

def create_user(value):

    novo_cliente = colecao.insert_one(value) #comando = f'INSERT INTO vendas (nome_produto, valor) VALUES ("{nome_produto}", {valor})'
    return "Usuário inseridpo com sucesso"


user = {
    "nome": "Ladiane Santana",
    "idade": 15,
    "altura": 168,
    "time_favoritos": ["remo", "paissandu"],

}

result = create_user(user)
print(result)