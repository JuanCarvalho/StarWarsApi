import datetime

from bson import ObjectId

data = [
    {
        "_id": ObjectId("6727b9062a4df9799e62dbda"),
        "titulo": "Uma Nova Esperança",
        "data_lancamento": "1977-05-25",
        "diretor": "George Lucas",
        "planetas": [ObjectId("6727b9062a4df9799e62dbd8"), ObjectId("6727b9062a4df9799e62dbd9")],
        "data_criacao": datetime.datetime(2024, 11, 3, 14, 55, 18, 458000),
        "data_ultima_alteracao": datetime.datetime(2024, 11, 3, 14, 55, 18, 458000),
    },
    {
        "_id": ObjectId("6727b9062a4df9799e62dbdb"),
        "titulo": "O Império Contra-Ataca",
        "data_lancamento": "1980-05-21",
        "diretor": "Irvin Kershner",
        "planetas": [ObjectId("6727b9062a4df9799e62dbd8")],
        "data_criacao": datetime.datetime(2024, 11, 3, 14, 55, 18, 458000),
        "data_ultima_alteracao": datetime.datetime(2024, 11, 3, 14, 55, 18, 458000),
    },
]

create_data = [
    {"titulo": "Uma Nova Esperança", "data_lancamento": "1977-05-25", "diretor": "George Lucas"},
    {
        "titulo": "O Império Contra-Ataca",
        "data_lancamento": "1980-05-21",
        "diretor": "Irvin Kershner",
        "planetas": [{"nome": "Tatooine", "clima": "arido", "diametro": 10465, "populacao": 200000}],
    },
    {
        "titulo": "O Retorno de Jedi",
        "data_lancamento": "1983-05-25",
        "diretor": "Richard Marquand",
        "planetas": ["6727b9062a4df9799e62dbda"],
    },
]
