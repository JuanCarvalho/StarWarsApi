from bson import ObjectId

from app.factories import port_factory


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
