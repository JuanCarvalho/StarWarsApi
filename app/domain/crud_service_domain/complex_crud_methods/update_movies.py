from bson import ObjectId

from app.factories import port_factory


class ProcessUpdateMovies:
    def __init__(self):
        self.port_movies = port_factory.create("crud_port_output", table_name="filmes")
        self.port_planets = port_factory.create("crud_port_output", table_name="planetas")

    def process_update(self, movie_id: str, update_data: dict) -> dict:
        """
        Processa a atualização de um filme, verificando se todos os planetas existem
        antes de realizar a atualização.
        """
        # Verificar se o filme existe
        existing_movie = self.port_movies.get(movie_id)
        if not existing_movie:
            raise ValueError(f"Filme com ID {movie_id} não encontrado")

        # Obter e validar a lista de planetas
        planetas_data = update_data.pop("planetas") or []
        planetas_ids = []

        for planeta_id in planetas_data:
            # Todos os itens na lista devem ser IDs de planetas que já existem
            if isinstance(planeta_id, str):
                existing_planeta = self.port_planets.get(planeta_id)
                if not existing_planeta:
                    raise ValueError(f"Planeta com ID {planeta_id} não encontrado")
                planetas_ids.append(ObjectId(planeta_id))
            else:
                raise ValueError(f"Formato inválido para planeta: {planeta_id}")

        # Atualizar os dados do filme com os planetas processados
        if planetas_ids:
            update_data["planetas"] = planetas_ids

        # Realizar a atualização do filme
        updated_movie = self.port_movies.update(movie_id, update_data)

        return updated_movie
