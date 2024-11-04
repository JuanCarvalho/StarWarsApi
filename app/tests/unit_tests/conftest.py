import pytest

from app.tests.conftest import load_asset_data


@pytest.fixture
def mongodb_health_check_method(mocker):
    return mocker.patch(
        "app.adapters.repository.mongo_db_repository.mongodb_repository.MongoDBRepository.health_check",
        return_value={"status": "ok"},
    )


@pytest.fixture
def mocker_mongodb_collection(mocker):
    def _mocker_find(collection_name: str):
        return load_asset_data(collection_name)

    def _mocker_find_one(collection_name: str):
        return load_asset_data(collection_name)[0]

    def _mocker_insert_one(collection_name: str):
        return mocker.MagicMock(inserted_id="6727b9062a4df9799e62dbda")

    def mocker_update_one(collection_name: str):
        return mocker.MagicMock(modified_count=1)

    def _mocker_get_collection(collection_name: str):
        _collection = mocker.MagicMock()
        _collection.find.return_value = _mocker_find(collection_name)
        _collection.find_one.return_value = _mocker_find_one(collection_name)
        _collection.insert_one.return_value = _mocker_insert_one(collection_name)
        _collection.update_one.return_value = mocker_update_one(collection_name)
        return _collection

    mocker_collection = mocker.patch(
        "app.adapters.repository.mongo_db_repository.mongodb_repository.MongoDBRepository.get_collection",
        side_effect=_mocker_get_collection,
    )
    return mocker_collection
