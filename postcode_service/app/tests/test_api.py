from fastapi.testclient import TestClient

from main import app, API_PREFIX
from .conftests import data_from_storage_service


client = TestClient(app)


def test_returns_locations_with_postcodes(data_from_storage_service):
    expected_result = [
        {"long": -2.08205, "lat": 51.905654, "postcode": "GL50 1PP"},
        {"long": -0.964052, "lat": 51.284118, "postcode": "RG27 9JU"}
    ]
    response = client.post(
        f'{API_PREFIX}/combine/', json=data_from_storage_service
    )
    assert response.status_code == 200
    assert response.json() == expected_result
