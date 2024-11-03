import pytest


@pytest.mark.usefixtures("disable_db_connection")
class TestRouters:
    def test_health_check(self, client, mongodb_health_check_method):
        response = client.get("/health/")
        assert response.status_code == 200
        assert response.json == {"status": "ok"}
        mongodb_health_check_method.assert_called_once()

    @pytest.mark.parametrize("table_name", ["planet", "movie"])
    def test_list(self, client, table_name):
        response = client.get(f"/{table_name}/")
        assert response.status_code == 200
