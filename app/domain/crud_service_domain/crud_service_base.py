from app.factories import port_factory


class CrudServiceBase:
    def __init__(self):
        self.crud_port_output = port_factory.create("crud_port_output")

    def health_check(self):
        return self.crud_port_output.health_check()

    def get(self, id: int):
        return self.crud_port_output.get(id)

    def list(self, filters: dict):
        return self.crud_port_output.list(filters)
