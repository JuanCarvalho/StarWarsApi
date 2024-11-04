from bson import ObjectId
from app.factories import port_factory


class ProcessUpdatePlanets:
    def __init__(self):
        self.port_planets = port_factory.create("crud_port_output", table_name="planetas")
        self.port_movies = port_factory.create("crud_port_output", table_name="filmes")

    def process_update(self, planet_id: str, update_data: dict) -> dict:
        """
        Processa a atualização de um planeta, verificando se todos os filmes existem
        antes de realizar a atualização.
        """
        # Verificar se o planeta existe
        existing_planet = self.port_planets.get(planet_id)
        if not existing_planet:
            raise ValueError(f"Planeta com ID {planet_id} não encontrado")

        # Obter e validar a lista de filmes
        filmes_data = update_data.pop("filmes") or []
        filmes_ids = []

        for filme_id in filmes_data:
            # Todos os itens na lista devem ser IDs de filmes que já existem
            if isinstance(filme_id, str):
                existing_filme = self.port_movies.get(filme_id)
                if not existing_filme:
                    raise ValueError(f"Filme com ID {filme_id} não encontrado")
                filmes_ids.append(ObjectId(filme_id))
            else:
                raise ValueError(f"Formato inválido para filme: {filme_id}")

        # Atualizar os dados do planeta com os filmes processados
        if filmes_ids:
            update_data["filmes"] = filmes_ids

        # Realizar a atualização do planeta
        updated_planet = self.port_planets.update(planet_id, update_data)

        return updated_planet
