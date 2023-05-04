from fastapi.testclient import TestClient
from server.FastApi.app.main import app

def test_pong():
    client = TestClient(app)
    result = client.get('/ping')
    assert result.status_code == 200
    assert result.json() == {'message': 'pong'}