from fastapi.testclient import TestClient

from main import app, API_PREFIX


client = TestClient(app)


def test_ACCEPTED_RESPONSE_when_start_update():
    response = client.post(f'{API_PREFIX}/start-update/')
    assert response.status_code == 202
