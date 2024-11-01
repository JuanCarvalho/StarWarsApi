import pytest

from app.config.flask_setup import create_app


@pytest.fixture
def app():
    """Cria uma instância da aplicação Flask para os testes."""
    app = create_app()

    # Configurações específicas para rodar os testes, se necessário
    app.config.update(
        {
            "TESTING": True,
        }
    )

    yield app


@pytest.fixture
def client(app):
    """Cria um cliente de teste para a aplicação Flask."""
    with app.test_client() as client:
        yield client
