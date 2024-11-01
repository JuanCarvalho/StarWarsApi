from flask import Flask

from app.common.flask_routers.health_routers import health_bp


def create_app():
    # Inicializa a aplicação Flask
    app = Flask(__name__)

    app.config["DEBUG"] = True

    # Registra as rotas da aplicação
    register_routes(app)

    return app


def register_routes(app):
    # Registra o blueprint da rota de health check
    app.register_blueprint(health_bp)
