from fastapi.testclient import TestClient

from app.main import add, app

client = TestClient(app)


def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "environment check"}


def test_health():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok, now this the second commit of mine to show how the CI/CD that we designed works"}


def test_add():
    assert add(2, 3) == 5


def test_add_negative():
    assert add(-1, 1) == 0