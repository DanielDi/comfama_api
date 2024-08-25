from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_create_afiliado():
    response = client.post(
        "/afiliados/",
        json={"nombres": "Juan", "apellidos": "Pérez", "email": "juan.perez@example.com", "estado": "activo"},
    )
    assert response.status_code == 200
    assert response.json()["email"] == "juan.perez@example.com"

def test_read_afiliados():
    response = client.get("/afiliados/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)