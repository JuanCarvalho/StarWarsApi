import pytest
import os
import json

from app.config.flask_setup import app as flask_app
from app.config.load_routers import *  # noqa
from app.factories import load_factories  # noqa


@pytest.fixture
def app():
    """Cria uma instância da aplicação Flask para os testes."""

    # Configurações específicas para rodar os testes, se necessário
    flask_app.config.update(
        {
            "TESTING": True,
        }
    )

    yield flask_app


@pytest.fixture
def client(app):
    """Cria um cliente de teste para a aplicação Flask."""
    with app.test_client() as client:
        yield client


@pytest.fixture
def mocker_db_connection(mocker):
    mocker.patch(
        "app.adapters.repository.mongo_db_repository.mongodb_repository.MongoDBRepository.db_connection",
        side_effect=mocker.Mock(),
    )


def load_asset_data(asset_name: str):
    """
    Carrega os arquivos JSON da pasta test/assets
    """
    try:
        module = __import__("app.tests.assets", fromlist=[asset_name])
        return getattr(module, asset_name).data
    except Exception as e:
        raise Exception(f"Erro ao carregar o asset {asset_name}: {e}")
