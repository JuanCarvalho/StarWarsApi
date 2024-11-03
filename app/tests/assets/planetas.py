import datetime
from bson import ObjectId

data = [
    {'_id': ObjectId('6727b9062a4df9799e62dbd8'), 'nome': 'Tatooine', 'clima': 'arido', 'diametro': 10465, 'populacao': 200000,
     'filmes': [ObjectId('6727b9062a4df9799e62dbda'), ObjectId('6727b9062a4df9799e62dbdb')],
     'data_criacao': datetime.datetime(2024, 11, 3, 14, 55, 18, 442000),
     'data_ultima_alteracao': datetime.datetime(2024, 11, 3, 14, 55, 18, 477000)},
    {'_id': ObjectId('6727b9062a4df9799e62dbd9'), 'nome': 'Alderaan', 'clima': 'temperado', 'diametro': 12500, 'populacao': 2000000000,
     'filmes': [ObjectId('6727b9062a4df9799e62dbda')], 'data_criacao': datetime.datetime(2024, 11, 3, 14, 55, 18, 442000),
     'data_ultima_alteracao': datetime.datetime(2024, 11, 3, 14, 55, 18, 478000)},
]
