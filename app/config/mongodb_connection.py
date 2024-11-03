import pymongo

from app.config.settings import settings


class MongoDBConnection:
    def __init__(self):
        self.client = pymongo.MongoClient(f"mongodb://{settings.mongodb_host}:{settings.mongodb_port}")  # type: ignore

    def db(self, db_name: str):
        return self.client[db_name]

    def collection(self, db_name: str, collection_name: str):
        if not collection_name:
            return None
        return self.db(db_name)[collection_name]
