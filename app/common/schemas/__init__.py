from app.common.schemas.movies_schema import MoviesCreateSchema, MoviesSchema, MoviesUpdateSchema
from app.common.schemas.planet_schema import PlanetCreateSchema, PlanetSchema, PlanetUpdateSchema

# Rebuild models para suprimir erro de importação circular
MoviesCreateSchema.model_rebuild()
PlanetCreateSchema.model_rebuild()
MoviesUpdateSchema.model_rebuild()
PlanetUpdateSchema.model_rebuild()


def schema_mapping(table_name: str):
    # TODO: Implementar com factory
    try:
        return {"filmes": MoviesSchema, "planetas": PlanetSchema}[table_name]
    except KeyError:
        raise Exception("Schema not found")


def schema_mapping_create_update(table_name: str, type_schema: str):
    # Reconstruindo o modelo após definição

    try:
        return {
            "filmes": {"create": MoviesCreateSchema, "update": MoviesUpdateSchema},  # type: ignore
            "planetas": {"create": PlanetCreateSchema, "update": PlanetUpdateSchema},  # type: ignore
        }[table_name][type_schema]
    except KeyError:
        raise Exception("Schema not found")
