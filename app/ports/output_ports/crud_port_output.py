from datetime import datetime

from app.adapters import NoSqlRepositoryContract
from app.common.schemas import schema_mapping
from app.factories import port_factory, repository_factory


@port_factory.register("crud_port_output")
class CrudPortOutput:

    def __init__(self, table_name: str | None = None):
        self.table_name = table_name
        self.repository: NoSqlRepositoryContract = repository_factory.create("mongodb_repository", collection_name=table_name)

    def serialize_data(self, response_data: dict | list):
        # TODO: Implementar com factory ou decorator
        if not self.table_name:
            return response_data
        serializer = schema_mapping(self.table_name)
        if isinstance(response_data, list):
            return [serializer.from_mongo(data).dict() for data in response_data]
        return serializer.from_mongo(response_data).dict()

    def health_check(self):
        return self.repository.health_check()

    def get(self, id: str):
        return self.serialize_data(self.repository.get(id))

    def list(self, filters: dict | None = None):
        return self.serialize_data(self.repository.list(filters))

    def create(self, data: dict):
        data_criacao = datetime.now()
        data.update({"data_criacao": data_criacao})
        data.update({"data_ultima_alteracao": data_criacao})
        response = self.repository.create(data)
        return str(response.inserted_id)

    def update(self, id: str, data: dict):
        data.update({"data_ultima_alteracao": datetime.now()})
        response = self.repository.update(id, data)
        return {"modified_count": response.modified_count}

    def delete(self, id: str):
        response = self.repository.delete(id)
        return {"deleted_count": response.deleted_count}
