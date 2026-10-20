import pytest
from app import app, store


@pytest.fixture(autouse=True)
def reset_store():
    store._tasks.clear()
    store._next_id = 1
    yield
    store._tasks.clear()
    store._next_id = 1


@pytest.fixture()
def client():
    app.config.update(TESTING=True)
    with app.test_client() as test_client:
        yield test_client


def test_index_returns_application_name(client):
    response = client.get("/")
    assert response.status_code == 200
    assert response.get_json()["application"] == "SecureTask API"


def test_create_and_list_task(client):
    created = client.post("/tasks", json={"title": "Belajar DevSecOps"})
    assert created.status_code == 201
    assert created.get_json()["task"]["title"] == "Belajar DevSecOps"

    listed = client.get("/tasks")
    assert len(listed.get_json()["tasks"]) == 1


def test_reject_empty_title(client):
    response = client.post("/tasks", json={"title": "   "})
    assert response.status_code == 400
    assert "error" in response.get_json()


def test_reject_non_object_json(client):
    response = client.post("/tasks", json=["bukan", "object"])
    assert response.status_code == 400


def test_delete_missing_task_returns_404(client):
    response = client.delete("/tasks/999")
    assert response.status_code == 404
