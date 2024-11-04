from app.domain.crud_service_domain.complex_crud_methods.create_movies import ProcessCreateMovies
from app.domain.crud_service_domain.complex_crud_methods.create_planets import ProcessCreatePlanets
from app.domain.crud_service_domain.complex_crud_methods.update_movies import ProcessUpdateMovies
from app.domain.crud_service_domain.complex_crud_methods.update_planets import ProcessUpdatePlanets
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
        # TODO: Remover esse if e utilizar factory
        if self.table_name == "planetas":
            planet_creator = ProcessCreatePlanets()
            return planet_creator.process_create(data)
        elif self.table_name == "filmes":
            movie_creator = ProcessCreateMovies()
            return movie_creator.process_create(data)
        else:
            return self.crud_port_output.create(data)

    def update(self, id: str, data: dict):
        # TODO: Remover esse if e utilizar factory
        if self.table_name == "planetas":
            planet_update = ProcessUpdatePlanets()
            return planet_update.process_update(id, data)
        elif self.table_name == "filmes":
            movie_update = ProcessUpdateMovies()
            return movie_update.process_update(id, data)
        else:
            return self.crud_port_output.update(id, data)

    def delete(self, id: str):
        return self.crud_port_output.delete(id)
