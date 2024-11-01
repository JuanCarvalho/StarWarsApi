from app.config.mongodb_connection import MongoDBConnection
from app.factories import repository_factory


@repository_factory.register("mongodb_repository")
class MongoDBRepository:
    def __init__(self, collection_name: str = "star_wars"):
        self.collection = self.get_collection(collection_name)

    @property
    def db_connection(self):
        return MongoDBConnection()

    def get_collection(self, collection_name: str):
        return self.db_connection.collection("star_wars", collection_name)

    def health_check_db(self):
        return self.db_connection.client.server_info()
