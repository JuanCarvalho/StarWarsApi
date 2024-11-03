from app.factories import port_factory


@port_factory.register("crud_input_port")
class CrudInputPort:
    def get(self, id: int):
        pass

    def list(self, filters: dict):
        pass
