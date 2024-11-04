import pytest

from app.tests.conftest import load_asset_data


@pytest.mark.usefixtures("mocker_db_connection")
class TestRouters:
    def test_health_check(self, client, mongodb_health_check_method):
        response = client.get("/health/")
        assert response.status_code == 200
        assert response.json == {"status": "ok"}
        mongodb_health_check_method.assert_called_once()

    @pytest.mark.parametrize("table_name", ["planet", "movie"])
    def test_list(self, client, table_name, mocker_mongodb_collection):
        response = client.get(f"/{table_name}/")
        assert response.status_code == 200
        mocker_mongodb_collection.assert_called_once()

    @pytest.mark.parametrize("table_name", ["planet", "movie"])
    def test_get(self, client, table_name, mocker_mongodb_collection):
        response = client.get(f"/{table_name}/6727b9062a4df9799e62dbda")
        assert response.status_code == 200
        mocker_mongodb_collection.assert_called_once()

    @pytest.mark.parametrize(
        "table_name_asset_name",
        [("planet", "planetas"), ("movie", "filmes")],
    )
    def test_create(self, client, table_name_asset_name, mocker_mongodb_collection):
        table_name, asset_name = table_name_asset_name
        create_data = load_asset_data(asset_name, "create_data")
        for data in create_data:
            response = client.post(f"/{table_name}/", json=data)
            assert response.status_code == 201

    @pytest.mark.parametrize(
        "table_name",
        ["planet", "movie"],
    )
    def test_update(self, client, table_name, mocker_mongodb_collection):
        _id = "6727b9062a4df9799e62dbda"
        update_data = {
            "foo": "bar",
        }
        response = client.put(f"/{table_name}/{_id}", json=update_data)
        assert response.status_code == 200
