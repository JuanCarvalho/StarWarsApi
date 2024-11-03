import pytest


@pytest.mark.usefixtures("mongodb_health_check_method")
def test_health_check(client):
    response = client.get("/health/")
    assert response.status_code == 200
    assert response.json == {"status": "ok"}
