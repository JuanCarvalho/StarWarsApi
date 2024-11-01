from datetime import datetime

from pymongo import MongoClient

# Conectando ao MongoDB (ajuste a URI conforme necessário)
client = MongoClient("mongodb://localhost:27017")
db = client["star_wars"]

# Criar coleções para Planetas e Filmes
planetas_collection = db["planetas"]
filmes_collection = db["filmes"]

# Inserir alguns Planetas
planetas = [
    {
        "nome": "Tatooine",
        "clima": "arido",
        "diametro": 10465,
        "populacao": 200000,
        "filmes": [],  # Vai ser atualizado depois com referências aos filmes
        "data_criacao": datetime.now(),
        "data_ultima_alteracao": datetime.now(),
    },
    {
        "nome": "Alderaan",
        "clima": "temperado",
        "diametro": 12500,
        "populacao": 2000000000,
        "filmes": [],
        "data_criacao": datetime.now(),
        "data_ultima_alteracao": datetime.now(),
    },
]

# Inserindo Planetas e salvando seus IDs
planetas_ids = planetas_collection.insert_many(planetas).inserted_ids

# Inserir alguns Filmes com referência aos planetas (relacionamento)
filmes = [
    {
        "titulo": "Uma Nova Esperança",
        "data_lancamento": "1977-05-25",
        "diretor": "George Lucas",
        "planetas": [planetas_ids[0], planetas_ids[1]],  # Referencia Tatooine e Alderaan
        "data_criacao": datetime.now(),
        "data_ultima_alteracao": datetime.now(),
    },
    {
        "titulo": "O Império Contra-Ataca",
        "data_lancamento": "1980-05-21",
        "diretor": "Irvin Kershner",
        "planetas": [planetas_ids[0]],  # Apenas Tatooine
        "data_criacao": datetime.now(),
        "data_ultima_alteracao": datetime.now(),
    },
]

# Inserindo Filmes
filmes_ids = filmes_collection.insert_many(filmes).inserted_ids

# Atualizar os planetas com os IDs dos filmes onde aparecem
for i, planeta in enumerate(planetas):
    filmes_relacionados = []
    for filme in filmes:
        if planetas_ids[i] in filme["planetas"]:
            filmes_relacionados.append(filmes_collection.find_one({"_id": filme["_id"]})["_id"])

    # Atualizando o planeta com as referências aos filmes
    planetas_collection.update_one(
        {"_id": planetas_ids[i]}, {"$set": {"filmes": filmes_relacionados, "data_ultima_alteracao": datetime.now()}}
    )

# Imprimir para verificar
for planeta in planetas_collection.find():
    print("Planeta:", planeta)

for filme in filmes_collection.find():
    print("Filme:", filme)
