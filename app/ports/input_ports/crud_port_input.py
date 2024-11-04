from typing import Literal

from pydantic import ValidationError

from app.common.exceptions.api_exceptions import BadRequest
from app.common.schemas import schema_mapping_create_update
from app.domain import CrudServiceContract
from app.factories import domain_factory, port_factory


@port_factory.register("crud_port_input")
class CrudPortInput:

    def __init__(self, table_name: str | None = None):
        self.table_name = table_name
        self.domain_service: CrudServiceContract = domain_factory.create("crud_default", table_name=table_name)

    def validate_data(self, data: dict, type_schema: Literal["create", "update"]):
        # TODO: Remover para uma classe de serialização e utilizar factory
        if not self.table_name:
            return data
        schema = schema_mapping_create_update(self.table_name, type_schema)
        try:
            return schema(**data).dict()
        except ValidationError as e:
            raise BadRequest(f"Invalid data: {e}")

    def health_check(self):
        return self.domain_service.health_check()

    def get(self, id: str):
        return self.domain_service.get(id)

    def list(self, filters: dict | None = None):
        return self.domain_service.list(filters)

    def create(self, data: dict):
        data = self.validate_data(data, "create")
        return self.domain_service.create(data)

    def update(self, id: str, data: dict):
        data = self.validate_data(data, "update")
        return self.domain_service.update(id, data)
