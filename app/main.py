from app.config.flask_setup import create_app
from app.factories.load_factories import *  # noqa

api_rest = create_app()

if __name__ == "__main__":
    # Inicializa o servidor
    api_rest.run(host="0.0.0.0", port=8000)  # Pode ajustar a porta se necessário
