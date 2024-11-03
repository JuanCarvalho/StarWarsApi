from flask import Flask
from flask_restx import Api

from app.common.flask_routers.health_routers import health_ns
from app.config.settings import settings


def create_app():
    # Inicializa a aplicação Flask
    app = Flask(__name__)

    app.config["DEBUG"] = True

    # Instância da API RestX e configuração do Swagger
    api = Api(app, title="Star Wars API", version=settings.api_version, description="A simple Star Wars API", doc="/docs")

    # Registra os namespaces
    register_routes(api, health_ns)

    return app


def register_routes(api, router):
    # Registra os namespaces
    api.add_namespace(router)
