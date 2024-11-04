from bson import ObjectId

from app.factories import port_factory


class ProcessCreateMovies:
    def __init__(self):
        self.port_movies = port_factory.create("crud_port_output", table_name="filmes")
        self.port_planets = port_factory.create("crud_port_output", table_name="planetas")

    def process_create(self, movie_data: dict) -> dict:
        """
        Processa a criação de um filme, verificando se planetas existem
        ou criando-os conforme necessário.
        """
        planetas_data = movie_data.pop("planetas") or []
        planetas_ids = []

        for planeta in planetas_data:
            if isinstance(planeta, dict):
                # Caso seja um novo planeta, validá-lo e criá-lo
                inserted_id = self.port_planets.create(planeta)
                planetas_ids.append(ObjectId(inserted_id))
            elif isinstance(planeta, str):
                # Caso seja um ID, validar se o planeta existe
                existing_planet = self.port_planets.get(planeta)
                if not existing_planet:
                    raise ValueError(f"Planeta com ID {planeta} não encontrado")
                planetas_ids.append(ObjectId(planeta))
            else:
                raise ValueError(f"Formato inválido para planeta: {planeta}")

        # Atualizar os dados do filme com os planetas processados
        if planetas_ids:
            movie_data["planetas"] = planetas_ids

        # Criar o filme
        created_movie = self.port_movies.create(movie_data)

        # Atualizar os planetas com o ID do filme
        for planeta_id in planetas_ids:
            planeta = self.port_planets.get(str(planeta_id))
            if planeta:
                planeta["filmes"].append(ObjectId(created_movie))
                self.port_planets.update(str(planeta_id), planeta)

        return created_movie


class ProcessCreatePlanets:
    def __init__(self):
        self.port_planets = port_factory.create("crud_port_output", table_name="planetas")
        self.port_movies = port_factory.create("crud_port_output", table_name="filmes")

    def process_create(self, planet_data: dict) -> dict:
        """
        Processa a criação de um planeta, verificando se filmes existem
        ou criando-os conforme necessário.
        """
        filmes_data = planet_data.pop("filmes") or []
        filmes_ids = []

        for filme in filmes_data:
            if isinstance(filme, dict):
                # Caso seja um novo filme, criá-lo
                inserted_id = self.port_movies.create(filme)
                filmes_ids.append(ObjectId(inserted_id))
            elif isinstance(filme, str):
                # Caso seja um ID, validar se o filme existe
                existing_filme = self.port_movies.get(filme)
                if not existing_filme:
                    raise ValueError(f"Filme com ID {filme} não encontrado")
                filmes_ids.append(ObjectId(filme))
            else:
                raise ValueError(f"Formato inválido para filme: {filme}")

        # Atualizar os dados do planeta com os filmes processados
        if filmes_ids:
            planet_data["filmes"] = filmes_ids

        # Criar o planeta
        created_planet = self.port_planets.create(planet_data)

        # Atualizar os filmes com o ID do planeta
        for filme_id in filmes_ids:
            filme = self.port_movies.get(str(filme_id))
            if filme:
                filme["planetas"].append(ObjectId(created_planet))
                self.port_movies.update(str(filme_id), filme)

        return created_planet


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
        if self.table_name == "planetas":
            planet_creator = ProcessCreatePlanets()
            return planet_creator.process_create(data)
        elif self.table_name == "filmes":
            movie_creator = ProcessCreateMovies()
            return movie_creator.process_create(data)
        else:
            return self.crud_port_output.create(data)
