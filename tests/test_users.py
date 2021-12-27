from fastapi.testclient import TestClient
from app.main import app
from app import schemas

client = TestClient(app)


def test_root():
    res = client.get("/")
    print(f'response is {res.json()}')
    assert res.json().get("message") == "welcome to my api"
    assert res.status_code == 200


def test_create_user():
    res = client.post(
        "/users/", json={"email": "pytest@example.com", "password": "pass12345"})
    print(f'post response is {res.json()}')
    new_user=schemas.UserOut(**res.json())
    assert new_user.email=="pytest@example.com"
    assert res.status_code == 201
