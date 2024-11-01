import pytest


@pytest.fixture
def mongodb_health_check_method(mocker):
    return mocker.patch(
        "app.adapters.repository.mongo_db_reposiroty.mongodb_repository.MongoDBRepository.health_check_db",
        return_value={"status": "db is ok"},
    )
