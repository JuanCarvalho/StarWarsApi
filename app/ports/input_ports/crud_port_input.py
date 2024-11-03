from app.factories import domain_factory, port_factory


@port_factory.register("crud_port_input")
class CrudPortInput:

    def domain_service(self, domain_service_name: str | None = None):
        if domain_service_name is not None:
            return domain_factory.create(domain_service_name)
        return domain_factory.create("crud_default")

    def health_check(self):
        return self.domain_service().health_check()

    def get(self, id: int):
        pass

    def list(self, filters: dict):
        pass
