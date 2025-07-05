from pymongo import MongoClient

URI = "mongodb+srv://valmir:X2QvyR3NfaRAeqB9@cluster0.kj6hvkk.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

client = MongoClient(URI)
db = client["clientes"]
col = db["users"]


def read_user():

    # response = col.count_documents({"nome": "Ladiane Santana"})

    response = col.find({})    # SELECT * FROM "users"

    for user in response:
        print(user)
    

    return response


result = read_user()

print(result)