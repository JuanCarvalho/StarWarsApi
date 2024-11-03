from app.common.schemas.movies_schema import MoviesSchema
from app.common.schemas.planet_schema import PlanetSchema


def schema_mapping(tabel_name: str):
    # TODO: Implementar com factory
    try:
        return {"filmes": MoviesSchema, "planetas": PlanetSchema}[tabel_name]
    except KeyError:
        raise Exception("Schema not found")
