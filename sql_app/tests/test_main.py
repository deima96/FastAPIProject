from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


# def test_get_users(mock_db_session):
#     response = client.get("/users")
#     assert response.status_code==200

def test_create_user(mock_db_session):
    response = client.post(
        "/users/",json={"email":"testemail", "password":"password"})
    assert response.status_code==200
    data=response.json()
    assert data["email"] == "testemail"
    assert data["password"] == "password"
    mock_db_session.add.assert_called()
    mock_db_session.commit.assert_called()


# def test_update_user():
#     response = client.put("/users/1",json={"email":"testemail", "password":"password"})
#     assert response.status_code==200
#
# def test_delete_user():
#     response = client.delete("/users/1")
#     assert response.status_code == 200
