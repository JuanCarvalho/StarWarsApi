from flask import Flask
from flask_restx import Api

from app.config.settings import settings


def create_app() -> Flask:
    # Inicializa a aplicação Flask
    flask_app = Flask(__name__)
    flask_app.config["DEBUG"] = True
    flask_app.url_map.strict_slashes = False
    return flask_app


def create_swagger(flask_app) -> Api:
    return Api(flask_app, title=settings.app_name, version=settings.api_version, description="A simple Star Wars API", doc="/docs")


app = create_app()
api = create_swagger(app)
