from bson import ObjectId

from app.config.mongodb_connection import MongoDBConnection
from app.factories import repository_factory


@repository_factory.register("mongodb_repository")
class MongoDBRepository:
    def __init__(self, collection_name: str | None = None):
        self.collection_name = collection_name

    def db_connection(self):
        return MongoDBConnection()

    def get_collection(self, collection_name: str | None = None):
        connection = self.db_connection()
        return connection.collection("star_wars", collection_name)

    def health_check(self):
        connection = self.db_connection()
        return connection.client.server_info()

    def get(self, id: str):
        collection = self.get_collection(self.collection_name)
        object_id = ObjectId(id)
        return collection.find_one({"_id": object_id})

    def list(self, filters: dict | None = None):
        if filters is None:
            filters = {}
        collection = self.get_collection(self.collection_name)
        return list(collection.find(filters))

    def create(self, data: dict):
        collection = self.get_collection(self.collection_name)
        return collection.insert_one(data)
