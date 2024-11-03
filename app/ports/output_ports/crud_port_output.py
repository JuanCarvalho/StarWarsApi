from app.adapters import NoSqlRepositoryContract
from app.factories import port_factory, repository_factory


@port_factory.register("crud_port_output")
class CrudPortOutput:

    def __init__(self):
        self.repository: NoSqlRepositoryContract = repository_factory.create("mongodb_repository")

    def health_check(self):
        return self.repository.health_check()

    def get(self, id: int):
        pass

    def list(self, filters: dict):
        pass
