from fastapi.testclient import TestClient

from backend.app.main import app

client = TestClient(app)


def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"msg": "Hello World"}

def test_convert_bad_source():
    response = client.get("/convert?source=foo&destination=K&value=10")
    assert response.status_code == 400
    assert response.json() == {'detail': 'Invalid source passed. Value must be one of "C", "K" or "F"'}

def test_convert_bad_destination():
    response = client.get("/convert?source=C&destination=101&value=10")
    assert response.status_code == 400
    assert response.json() == {'detail': 'Invalid destination passed. Value must be one of "C", "K" or "F"'}

def test_convert_bad_value():
    response = client.get("/convert?source=C&destination=K&value=abc")
    assert response.status_code == 400
    assert response.json() == {'detail': 'Invalid value passed. Value must be a valid Integer or Float only'}

def test_valid_input():
    response = client.get("/convert?source=C&destination=K&value=0")
    assert response.status_code == 200
    assert response.text == '273.0'