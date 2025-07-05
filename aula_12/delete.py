from pymongo import MongoClient

USER = "valmir"
PASSWORD = "X2QvyR3NfaRAeqB9"

URI = f"mongodb+srv://{USER}:{PASSWORD}@cluster0.kj6hvkk.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

client = MongoClient(URI)
db = client["clientes"]
colecao = db["users"]


def delete_user(value):

    # response = colecao.delete_one( 
    #     {"nome": value} 
    # )


    response = colecao.delete_many({}) # DELETE * FROM users
    


    return "Usuário deletado com sucesso!"


user = "Ladiane Santana"


print(delete_user(user))