from app.factories import port_factory


class CrudServiceBase:
    def __init__(self, table_name: str | None = None):
        self.table_name = table_name
        self.crud_port_output = port_factory.create("crud_port_output", table_name=table_name)

    def health_check(self):
        return self.crud_port_output.health_check()

    def get(self, id: str):
        return self.crud_port_output.get(id)

    def list(self, filters: dict | None = None):
        return self.crud_port_output.list(filters)

    def create(self, data: dict):
        return self.crud_port_output.create(data)
