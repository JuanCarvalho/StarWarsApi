from app.domain import CrudServiceContract
from app.factories import domain_factory, port_factory


@port_factory.register("crud_port_input")
class CrudPortInput:

    def __init__(self, table_name: str | None = None):
        self.table_name = table_name
        self.domain_service: CrudServiceContract = domain_factory.create("crud_default", table_name=table_name)

    def health_check(self):
        return self.domain_service.health_check()

    def get(self, id: str):
        return self.domain_service.get(id)

    def list(self, filters: dict | None = None):
        return self.domain_service.list(filters)
