from app.config.flask_setup import app as api_rest
from app.config.load_routers import *  # noqa
from app.factories.load_factories import *  # noqa

if __name__ == "__main__":
    # Inicializa o servidor
    api_rest.run(host="0.0.0.0", port=8000)  # Pode ajustar a porta se necessário
