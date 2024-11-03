import pytest


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
