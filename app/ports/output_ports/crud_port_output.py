from app.common.schemas import schema_mapping
from app.factories import port_factory, repository_factory


@port_factory.register("crud_port_output")
class CrudPortOutput:

    def __init__(self, table_name: str | None = None):
        self.table_name = table_name
        self.repository = repository_factory.create("mongodb_repository", collection_name=table_name)

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

    def get(self, id: int):
        return self.repository.get(id)

    def list(self, filters: dict | None = None):
        return self.serialize_data(self.repository.list(filters))
