from app.common.flask_routers.health_routers import health_ns
from app.common.flask_routers.movies_routers import movies_ns
from app.common.flask_routers.planet_routers import planets_ns
from app.config.flask_setup import api as restx_api


def register_routes(api, router):
    api.add_namespace(router)


# Registra os namespaces
register_routes(restx_api, health_ns)
register_routes(restx_api, planets_ns)
register_routes(restx_api, movies_ns)
