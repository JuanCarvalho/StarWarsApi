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
